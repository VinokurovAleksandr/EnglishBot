from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from bot.states import Survey
from bot.google_sheets import save_to_sheet
from bot.config import BOT_TOKEN
from bot import keyboards as kb
import aiohttp

router = Router()

# Reading confirmed
@router.message(Survey.read_confirm, F.text == "I read the text")
async def reading_q1(msg: Message, state: FSMContext):
    await msg.answer("📘 Q1: What has contributed to the growth of remote work?", reply_markup=kb.reading_q1_kb)
    await state.set_state(Survey.reading_q1)

@router.message(Survey.reading_q1)
async def reading_q2(msg: Message, state: FSMContext):
    await state.update_data(reading_q1=msg.text)
    await msg.answer("📘 Q2: What are some benefits of remote work for employees?", reply_markup=kb.reading_q2_kb)
    await state.set_state(Survey.reading_q2)

@router.message(Survey.reading_q2)
async def reading_q3(msg: Message, state: FSMContext):
    await state.update_data(reading_q2=msg.text)
    await msg.answer("📘 Q3: Why might some employees feel isolated?", reply_markup=kb.reading_q3_kb)
    await state.set_state(Survey.reading_q3)

@router.message(Survey.reading_q3)
async def reading_q4(msg: Message, state: FSMContext):
    await state.update_data(reading_q3=msg.text)
    await msg.answer("📘 Q4: What do companies need to invest in?", reply_markup=kb.reading_q4_kb)
    await state.set_state(Survey.reading_q4)

# @router.message(Survey.reading_q4)
# async def ask_connection(msg: Message, state: FSMContext):
#     await state.update_data(reading_q4=msg.text)
#     await msg.answer("💬 What can help maintain a sense of connection and teamwork in remote teams?")
#     await state.set_state(Survey.connection)

@router.message(Survey.reading_q4)
async def ask_essay1(msg: Message, state: FSMContext):
    await state.update_data(reading_q4=msg.text)
    await msg.answer("📝 Write an answer on the following topic:\n\n"
                     "1. The advantages and disadvantages of remote work\n\n"
                     "2. Your ideal work environment and why\n\n",
                      reply_markup=ReplyKeyboardRemove())
    await state.set_state(Survey.essay1)


@router.message(Survey.essay1)
async def after_reading(msg: Message, state: FSMContext):
    await state.update_data(essay1=msg.text)
    await msg.answer("📘 And now the grammatical part ✍️")
    await msg.answer("📙 1. By next year, more companies __________ (offer) remote work options to their employees.",
                     reply_markup=kb.grammar_q1_kb)
    await state.set_state(Survey.grammar_q1)

@router.message(Survey.essay1)
async def grammar_q1(msg: Message, state: FSMContext):
    await state.update_data(essay2=msg.text)
    await msg.answer("📙 1. By next year, more companies __________ (offer) remote work options to their employees.", reply_markup=kb.grammar_q1_kb)
    await state.set_state(Survey.grammar_q1)

@router.message(Survey.grammar_q1)
async def grammar_q2(msg: Message, state: FSMContext):
    await state.update_data(grammar_q1=msg.text)
    await msg.answer("📙 2. She always __________ (use) video conferencing to communicate with her team.", reply_markup=kb.grammar_q2_kb)
    await state.set_state(Survey.grammar_q2)

@router.message(Survey.grammar_q2)
async def grammar_q3(msg: Message, state: FSMContext):
    await state.update_data(grammar_q2=msg.text)
    await msg.answer("📙 3. They __________ (implement) new remote work policies next month.", reply_markup=kb.grammar_q3_kb)
    await state.set_state(Survey.grammar_q3)

@router.message(Survey.grammar_q3)
async def grammar_q4(msg: Message, state: FSMContext):
    await state.update_data(grammar_q3=msg.text)
    await msg.answer("📙 4. The company __________ (invest) in new technology by the end of the year.", reply_markup=kb.grammar_q4_kb)
    await state.set_state(Survey.grammar_q4)

@router.message(Survey.grammar_q4)
async def grammar_q5(msg: Message, state: FSMContext):
    await state.update_data(grammar_q4=msg.text)
    await msg.answer("📙 5. __________ you ever __________ (work) remotely before?", reply_markup=kb.grammar_q5_kb)
    await state.set_state(Survey.grammar_q5)

@router.message(Survey.grammar_q5)
async def ask_voice(msg: Message, state: FSMContext):
    await state.update_data(grammar_q5=msg.text)
    await msg.answer("🎤 Prepare a short speech (2-3 minutes) on one of the following topics:\n\n"
                     "1. The benefits of remote work\n\n"
                     "2. How to stay connected while working remotely\n\n"
                     "3. The future of work\n\n"
                    "🎙 Please send your answer as a voice message.\n\n")
    await state.set_state(Survey.voice)

@router.message(Survey.voice, F.voice)
async def handle_voice(msg: Message, state: FSMContext, bot):
    file_id = msg.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    audio_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

    await state.update_data(audio_file_url=audio_url)
    data = await state.get_data()
    save_to_sheet(data)
    await msg.answer("✅ Looking forward to see you!.")
    await state.clear()