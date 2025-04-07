from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from bot.states import Survey
from bot import keyboards as kb
from bot.google_sheets import save_to_sheet
from bot.config import BOT_TOKEN

router = Router()

@router.message(F.text.lower().contains("A1"))
async def start_a1(msg: Message, state: FSMContext):
    await msg.answer("📘 Read the text and answer the questions.\n\n(Прочитайте текст та дайте відповіді на запитання)")
    await msg.answer(
        "Liam is a teacher. He works from Monday to Friday, but his weekends are always exciting. "
        "On Saturday morning, he goes jogging in the park. After that, he has breakfast at his favorite café. "
        "In the afternoon, he meets his friends, and they go to the cinema or visit a museum. On Sunday, Liam usually stays at home. "
        "He cleans his apartment, reads books, and sometimes learns new recipes. In the evening, he watches TV or listens to music."
    )
    await msg.answer("1. What does Liam do on Saturday mornings?", reply_markup=kb.a1_q1_kb)
    await state.set_state(Survey.a1_q1)

@router.message(Survey.a1_q1)
async def a1_q2(msg: Message, state: FSMContext):
    await state.update_data(a1_q1=msg.text)
    await msg.answer("2. Where does Liam have breakfast on Saturdays?", reply_markup=kb.a1_q2_kb)
    await state.set_state(Survey.a1_q2)

@router.message(Survey.a1_q2)
async def a1_q3(msg: Message, state: FSMContext):
    await state.update_data(a1_q2=msg.text)
    await msg.answer("3. What does Liam do in the afternoon on Saturdays?", reply_markup=kb.a1_q3_kb)
    await state.set_state(Survey.a1_q3)

@router.message(Survey.a1_q3)
async def a1_q4(msg: Message, state: FSMContext):
    await state.update_data(a1_q3=msg.text)
    await msg.answer("4. What does Liam do on Sunday?", reply_markup=kb.a1_q4_kb)
    await state.set_state(Survey.a1_q4)

@router.message(Survey.a1_q4)
async def a1_q5(msg: Message, state: FSMContext):
    await state.update_data(a1_q4=msg.text)
    await msg.answer("5. What does Liam do in the evening on Sundays?", reply_markup=kb.a1_q5_kb)
    await state.set_state(Survey.a1_q5)

@router.message(Survey.a1_q5)
async def a1_voice_intro(msg: Message, state: FSMContext):
    await state.update_data(a1_q5=msg.text)
    await msg.answer("🎤 Speaking:\n(Запишіть голосове повідомлення та дайте відповіді на запитання)")
    await msg.answer(
        "1. Describe your daily routine in detail.\n"
        "2. Talk about your last weekend. What did you do?\n"
        "3. Describe a place you visited. What did you see and do there?\n"
        "4. What are your plans for next weekend?\n"
        "5. Tell me about your favorite hobby. Why do you like it?"
    )
    await state.set_state(Survey.a1_voice)

@router.message(Survey.a1_voice, F.voice)
async def a1_grammar1(msg: Message, state: FSMContext, bot):
    file_id = msg.voice.file_id
    file = await bot.get_file(file_id)
    voice_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file.file_path}"
    await state.update_data(a1_voice_url=voice_url)
    await msg.answer("📘 Choose the correct answer: (Оберіть правильну відповідь)")
    await msg.answer("1. Lisa __ to school by bus every morning.", reply_markup=kb.a1_g1_kb)
    await state.set_state(Survey.a1_g1)

@router.message(Survey.a1_g1)
async def a1_g2(msg: Message, state: FSMContext):
    await state.update_data(a1_g1=msg.text)
    await msg.answer("2. We __ to the beach last summer.", reply_markup=kb.a1_g2_kb)
    await state.set_state(Survey.a1_g2)

@router.message(Survey.a1_g2)
async def a1_g3(msg: Message, state: FSMContext):
    await state.update_data(a1_g2=msg.text)
    await msg.answer("3. __ you ever been to another country?", reply_markup=kb.a1_g3_kb)
    await state.set_state(Survey.a1_g3)

@router.message(Survey.a1_g3)
async def a1_g4(msg: Message, state: FSMContext):
    await state.update_data(a1_g3=msg.text)
    await msg.answer("4. If it __ tomorrow, we will stay at home.", reply_markup=kb.a1_g4_kb)
    await state.set_state(Survey.a1_g4)

@router.message(Survey.a1_g4)
async def a1_g5(msg: Message, state: FSMContext):
    await state.update_data(a1_g4=msg.text)
    await msg.answer("5. They __ dinner when I called them.", reply_markup=kb.a1_g5_kb)
    await state.set_state(Survey.a1_g5)

@router.message(Survey.a1_g5)
async def a1_open_q1(msg: Message, state: FSMContext):
    await state.update_data(a1_g5=msg.text)
    await msg.answer("📘 Choose the correct word to complete the sentence.\n(Впишіть правильне слово)")
    await msg.answer("1. The opposite of 'early' is __.")
    await state.set_state(Survey.a1_open_1)

@router.message(Survey.a1_open_1)
async def a1_open_q2(msg: Message, state: FSMContext):
    await state.update_data(a1_open_1=msg.text)
    await msg.answer("2. A person who writes books is a __.")
    await state.set_state(Survey.a1_open_2)

@router.message(Survey.a1_open_2)
async def a1_open_q3(msg: Message, state: FSMContext):
    await state.update_data(a1_open_2=msg.text)
    await msg.answer("3. We need a __ to enter another country.")
    await state.set_state(Survey.a1_open_3)

@router.message(Survey.a1_open_3)
async def a1_open_q4(msg: Message, state: FSMContext):
    await state.update_data(a1_open_3=msg.text)
    await msg.answer("4. My grandmother is __ years old. (use letters to write a number)")
    await state.set_state(Survey.a1_open_4)

@router.message(Survey.a1_open_4)
async def a1_open_q5(msg: Message, state: FSMContext):
    await state.update_data(a1_open_4=msg.text)
    await msg.answer("5. We go to the __ when we are sick.")
    await state.set_state(Survey.a1_open_5)

@router.message(Survey.a1_open_5)
async def a1_finish(msg: Message, state: FSMContext):
    await state.update_data(a1_open_5=msg.text)
    data = await state.get_data()
    save_to_sheet(data)
    await msg.answer("✅ Дякую! Ви завершили рівень A1! 🎉")
    await state.clear()