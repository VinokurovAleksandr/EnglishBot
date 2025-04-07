from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from bot.states import Survey
from bot import keyboards as kb
from bot.google_sheets import save_to_sheet
from bot.config import BOT_TOKEN

router = Router()

@router.message(F.text.contains("Pre-A1"))
async def start_pre_a1(msg: Message, state: FSMContext):
    await msg.answer("📘 Read the text and write down the answers:\n\n(Прочитайте текст та дайте відповіді на запитання)")
    await msg.answer("Anna is a teacher. She works in a school. She has a cat and a dog. Every morning, she drinks coffee and goes to work.")
    await msg.answer("✅ Натисніть кнопку нижче, коли прочитаєте текст.", reply_markup=kb.pre_a1_read_kb)
    await state.set_state(Survey.pre_a1_read_confirm)

@router.message(Survey.pre_a1_q5)
async def pre_a1_speaking_intro(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_q5=msg.text)
    await msg.answer("🎤 Speaking:\n(Запишіть голосове повідомлення та дайте відповіді на запитання)")
    await msg.answer(
        "1. Introduce yourself (name, age, job, country).\n"
        "2. Describe your family (who is in your family?).\n"
        "3. What do you do every day? (morning, afternoon, evening).\n"
        "4. Name three things you like and three things you don’t like.\n"
        "5. What is your favorite food? Why?"
    )
    await state.set_state(Survey.pre_a1_voice)

@router.message(Survey.pre_a1_voice, F.voice)
async def pre_a1_grammar_intro(msg: Message, state: FSMContext, bot):
    file_id = msg.voice.file_id
    file = await bot.get_file(file_id)
    voice_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file.file_path}"
    await state.update_data(pre_a1_voice_url=voice_url)

    await msg.answer("📘 Choose the correct option (Оберіть правильну відповідь)")
    await msg.answer("1. This is Sébastien. He's _______.", reply_markup=kb.pre_a1_g1_kb)
    await state.set_state(Survey.pre_a1_g1)
@router.message(Survey.pre_a1_g1)
async def pre_a1_g2(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g1=msg.text)
    await msg.answer("2. I love music but I _____ like TV.", reply_markup=kb.pre_a1_g2_kb)
    await state.set_state(Survey.pre_a1_g2)

@router.message(Survey.pre_a1_g2)
async def pre_a1_g3(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g2=msg.text)
    await msg.answer("3. ___ she like sport?", reply_markup=kb.pre_a1_g3_kb)
    await state.set_state(Survey.pre_a1_g3)

@router.message(Survey.pre_a1_g3)
async def pre_a1_g4(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g3=msg.text)
    await msg.answer("4. When ___ have lunch?", reply_markup=kb.pre_a1_g4_kb)
    await state.set_state(Survey.pre_a1_g4)

@router.message(Survey.pre_a1_g4)
async def pre_a1_g5(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g4=msg.text)
    await msg.answer("5. Do you like ____ DVDs?", reply_markup=kb.pre_a1_g5_kb)
    await state.set_state(Survey.pre_a1_g5)

@router.message(Survey.pre_a1_g5)
async def pre_a1_g6(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g5=msg.text)
    await msg.answer("6. They start ____ school at 8.00 in the morning.", reply_markup=kb.pre_a1_g6_kb)
    await state.set_state(Survey.pre_a1_g6)

@router.message(Survey.pre_a1_g6)
async def pre_a1_g7(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g6=msg.text)
    await msg.answer("7. Peter’s _________ name is Michael.", reply_markup=kb.pre_a1_g7_kb)
    await state.set_state(Survey.pre_a1_g7)

@router.message(Survey.pre_a1_g7)
async def pre_a1_g8(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g7=msg.text)
    await msg.answer("8. She’s very friendly but she______ very quiet.", reply_markup=kb.pre_a1_g8_kb)
    await state.set_state(Survey.pre_a1_g8)

@router.message(Survey.pre_a1_g8)
async def pre_a1_g9(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g8=msg.text)
    await msg.answer("9. He hasn't got _____ brothers and sisters.", reply_markup=kb.pre_a1_g9_kb)
    await state.set_state(Survey.pre_a1_g9)

@router.message(Survey.pre_a1_g9)
async def pre_a1_g10(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g9=msg.text)
    await msg.answer("10. They went to the beach with some friends ____ Sunday.", reply_markup=kb.pre_a1_g10_kb)
    await state.set_state(Survey.pre_a1_g10)

@router.message(Survey.pre_a1_g10)
async def pre_a1_finish(msg: Message, state: FSMContext):
    await state.update_data(pre_a1_g10=msg.text)
    data = await state.get_data()
    save_to_sheet(data)
    await msg.answer("✅ Дякуємо! Ви завершили Pre-A1 тест!")
    await state.clear()