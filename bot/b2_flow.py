from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from bot.states import Survey
from bot import keyboards as kb
from bot.google_sheets import save_to_sheet
from bot.config import BOT_TOKEN

router = Router()

@router.message(F.text.contains("B2"))
async def start_b2_flow(msg: Message, state: FSMContext):
    await msg.answer("🧠 Проведемо невеликий тест")
    await msg.answer("📖 Read the following passage and answer the questions below:")
    await msg.answer(
        "\"Atomic Habits\" focuses on the concept that tiny changes can lead to remarkable results. "
        "By making small, incremental improvements every day, individuals can transform their habits and achieve their goals. "
        "The book introduces the idea of habit stacking, which involves linking new habits to existing ones to make them easier to adopt. "
        "Clear also emphasizes the importance of identity in habit formation, suggesting that individuals should focus on becoming the type of person they want to be "
        "rather than just achieving specific outcomes. By understanding the four laws of behavior change—make it obvious, make it attractive, make it easy, and make it satisfying—"
        "people can create lasting positive habits and eliminate negative ones."
    )
    await msg.answer("✅Click the 'I read the text' button when you're done reading.", reply_markup=kb.b2_read_confirm_kb)
    await state.set_state(Survey.b2_read_confirm)

@router.message(Survey.b2_read_confirm, F.text == "I read the text")
async def b2_q1(msg: Message, state: FSMContext):
    await msg.answer("1. What is the main idea of 'Atomic Habits'?", reply_markup=kb.b2_q1_kb)
    await state.set_state(Survey.b2_q1)

@router.message(Survey.b2_q1)
async def b2_q2(msg: Message, state: FSMContext):
    await state.update_data(b2_q1=msg.text)
    await msg.answer("2. What is habit stacking?", reply_markup=kb.b2_q2_kb)
    await state.set_state(Survey.b2_q2)

@router.message(Survey.b2_q2)
async def b2_q3(msg: Message, state: FSMContext):
    await state.update_data(b2_q2=msg.text)
    await msg.answer("3. Why is identity important in habit formation according to the book?", reply_markup=kb.b2_q3_kb)
    await state.set_state(Survey.b2_q3)

@router.message(Survey.b2_q3)
async def b2_q4(msg: Message, state: FSMContext):
    await state.update_data(b2_q3=msg.text)
    await msg.answer("4. Which of the following is NOT one of the four laws of behavior change mentioned in the book?", reply_markup=kb.b2_q4_kb)
    await state.set_state(Survey.b2_q4)

@router.message(Survey.b2_q4)
async def b2_q5(msg: Message, state: FSMContext):
    await state.update_data(b2_q4=msg.text)
    await msg.answer("5. What is the purpose of making small, incremental improvements every day?", reply_markup=kb.b2_q5_kb)
    await state.set_state(Survey.b2_q5)

@router.message(Survey.b2_q5)
async def b2_essay_intro(msg: Message, state: FSMContext):
    await state.update_data(b2_q5=msg.text)
    await msg.answer(
        "📝 Write an answer on one of the following topics:\n\n",
        reply_markup=kb.b2_essay_topic_kb
    )
    await state.set_state(Survey.b2_essay_topic)

@router.message(Survey.b2_essay_topic)
async def b2_essay_answer(msg: Message, state: FSMContext):
    await state.update_data(b2_essay_topic=msg.text)
    await msg.answer("✍️ Write your answer below:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Survey.b2_essay_answer)

@router.message(Survey.b2_essay_answer)
async def b2_grammar_1(msg: Message, state: FSMContext):
    await state.update_data(b2_essay_answer=msg.text)
    await msg.answer(
        "📘 Choose the correct option to complete the sentences:"
        "1. By next month, I __________ (develop) several new positive habits using the principles from 'Atomic Habits.'"
        ,
        reply_markup=kb.b2_g1_kb
    )
    await state.set_state(Survey.b2_g1)

@router.message(Survey.b2_g1)
async def b2_grammar_2(msg: Message, state: FSMContext):
    await state.update_data(b2_g1=msg.text)
    await msg.answer("2. He always __________ (use) habit stacking to build new habits.", reply_markup=kb.b2_g2_kb)
    await state.set_state(Survey.b2_g2)

@router.message(Survey.b2_g2)
async def b2_grammar_3(msg: Message, state: FSMContext):
    await state.update_data(b2_g2=msg.text)
    await msg.answer("3. They __________ (adopt) the four laws of behavior change to improve their daily routines next week.", reply_markup=kb.b2_g3_kb)
    await state.set_state(Survey.b2_g3)

@router.message(Survey.b2_g3)
async def b2_grammar_4(msg: Message, state: FSMContext):
    await state.update_data(b2_g3=msg.text)
    await msg.answer("4. The author __________ (introduce) the concept of identity-based habits by the end of the book.", reply_markup=kb.b2_g4_kb)
    await state.set_state(Survey.b2_g4)

@router.message(Survey.b2_g4)
async def b2_grammar_5(msg: Message, state: FSMContext):
    await state.update_data(b2_g4=msg.text)
    await msg.answer("5. __________ you ever __________ (read) 'Atomic Habits' before?", reply_markup=kb.b2_g5_kb)
    await state.set_state(Survey.b2_g5)

@router.message(Survey.b2_g5)
async def b2_voice_prompt(msg: Message, state: FSMContext):
    await state.update_data(b2_g5=msg.text)
    await msg.answer(
        "🎤 Prepare a short speech (2–3 minutes) on one of the following topics:\n\n"
        "1. The benefits of applying the principles from 'Atomic Habits' to your daily life.\n\n"
        "2. How habit stacking can help you build new positive habits.\n\n"
        "3. The future of habit formation and behavior change based on the concepts in 'Atomic Habits.\n\n'"
        "🎙Send your response as a voice message."
    )
    await state.set_state(Survey.b2_voice)

@router.message(Survey.b2_voice, F.voice)
async def b2_voice_handler(msg: Message, state: FSMContext, bot):
    file_id = msg.voice.file_id
    file = await bot.get_file(file_id)
    voice_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file.file_path}"
    await state.update_data(b2_voice_url=voice_url)

    data = await state.get_data()
    save_to_sheet(data)

    await msg.answer("✅ Looking forward to see you!.")
    await state.clear()