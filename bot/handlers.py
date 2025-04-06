from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot.states import Survey
from bot import keyboards as kb
from bot.google_sheets import save_to_sheet

router = Router()



@router.message(Command("start"))
async def cmd_start(msg: Message, state: FSMContext):
    await msg.answer(
        "📚 *Вітаємо у боті-опитувальнику з вивчення англійської!* 🇬🇧\n\n"
        "Be ready,бо воно займе трохи твого часу-be patient \n\n"
        "Тут ти пройдеш коротке, але useful опитування для тебе і твого майбутнього викладача 🧠\n"
        "Ми дізнаємося більше про твої цілі, труднощі та вподобання у навчанні англійської мови.\n\n"
        "🎯 На основі твоїх відповідей ми зможемо підібрати для тебе кастомізовану програму навчання!\n\n"
        "👇 Натисни кнопку нижче, щоб розпочати!",
        reply_markup=kb.start_kb,
        parse_mode="Markdown"
    )

from bot import b1_flow
router.include_router(b1_flow.router)

from bot import b2_flow  # імпортуємо FSM-гілку B2
router.include_router(b2_flow.router)  # підключаємо до загального router



def register_handlers(dp):
    dp.include_router(router)

@router.message(F.text == "🚀 Почати опитування")
async def start_survey(msg: Message, state: FSMContext):
    await msg.answer("📌 Твоє твоє ім'я та прізвище?", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Survey.name)

@router.message(Survey.name)
async def ask_motivation(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("🤔 Чому ти хочеш  вивчати англійську саме зараз?")
    await state.set_state(Survey.motivation)

@router.message(Survey.motivation)
async def ask_obstacle(msg: Message, state: FSMContext):
    await state.update_data(motivation=msg.text)
    await msg.answer("🚧 Що для твою думку є найбільшою перешкодою у вивченні англійської?")
    await state.set_state(Survey.obstacle)

@router.message(Survey.obstacle)
async def ask_goal(msg: Message, state: FSMContext):
    await state.update_data(obstacle=msg.text)
    await msg.answer("🎯 Як ти плануєте використовувати свої знання англійської мови в майбутньому?")
    await state.set_state(Survey.goal)

@router.message(Survey.goal)
async def ask_interest(msg: Message, state: FSMContext):
    await state.update_data(goal=msg.text)
    await msg.answer("💡 Які аспекти англійської мови тебе цікавлять найбільше?", reply_markup=kb.interest_kb)
    await state.set_state(Survey.interest)

@router.message(Survey.interest)
async def ask_format(msg: Message, state: FSMContext):
    await state.update_data(interest=msg.text)
    await msg.answer("📘 Який формат навчання для тебе більше підходить?", reply_markup=kb.format_kb)
    await state.set_state(Survey.format)

@router.message(Survey.format)
async def ask_pace(msg: Message, state: FSMContext):
    await state.update_data(format=msg.text)
    await msg.answer("⏱️ Який темп навчання для тебе найбільш комфортний?", reply_markup=kb.pace_kb)
    await state.set_state(Survey.pace)

@router.message(Survey.pace)
async def ask_hobbies(msg: Message, state: FSMContext):
    await state.update_data(pace=msg.text)
    await msg.answer("🎨 Які в тебе хобі та інтереси?", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Survey.hobbies)

@router.message(Survey.hobbies)
async def ask_usage(msg: Message, state: FSMContext):
    await state.update_data(hobbies=msg.text)
    await msg.answer("🗣 Як часто ти використовуєте англійську мову в повсякденному житті?")
    await state.set_state(Survey.usage)

@router.message(Survey.usage)
async def ask_favorites(msg: Message, state: FSMContext):
    await state.update_data(usage=msg.text)
    await msg.answer("🎬 Які твої улюблені фільми, книги, музика англійською мовою?")
    await state.set_state(Survey.favorites)

@router.message(Survey.favorites)
async def ask_level(msg: Message, state: FSMContext):
    await state.update_data(favorites=msg.text)
    await msg.answer("📊 На твою думку, який в тебе рівень англійської?", reply_markup=kb.level_kb)
    await state.set_state(Survey.level)

# @router.message(Survey.level)
# async def handle_level(msg: Message, state: FSMContext):
#     await state.update_data(level=msg.text)
#     # 
#     if "B1" in msg.text:
#         await msg.answer("📖 Read the following passage and answer the questions below:\n\n"
#                          "⬇️"
#                          "In recent years, the popularity of remote work has grown significantly. "
#                          "With advances in technology and communication tools, more companies are offering employees the flexibility to work from home or other locations. "
#                          "This shift has been driven by several factors, including the desire for a better work-life balance, reduced commuting time, and the ability to attract talent from a broader geographic area.\n\n"
                        
#                          "Remote work offers numerous benefits for both employers and employees. "
#                          "Employees often report higher job satisfaction, increased productivity, and reduced stress levels. "
#                          "Employers can save on office space and related expenses, and they can also access a larger pool of candidates for open positions.\n\n"
                  
#                          "However, remote work also presents challenges."
#                          "Some employees may feel isolated or disconnected from their colleagues, which can impact collaboration and team cohesion. "
#                          "Additionally, managing remote teams requires different skills and strategies compared to traditional office settings."
                         
#                          )
        
#         await msg.answer(
#             "✅ Натисни кнопку 'I read the text' коли прочитаєш.",
#               reply_markup=ReplyKeyboardMarkup(
#             keyboard=[[KeyboardButton(text="I read the text")]], 
#             resize_keyboard=True,
#             one_time_keyboard=True
#         ))
#         await state.set_state(Survey.read_confirm)
#     else:
#         # Якщо не B1 – просто зберігаємо відповіді
#         data = await state.get_data()
#         save_to_sheet(data)
#         await msg.answer("✅ Дякуємо за ваші відповіді!")
#         await state.clear()

@router.message(Survey.level)
async def handle_level(msg: Message, state: FSMContext):
    await state.update_data(level=msg.text)

    if "B1" in msg.text:
        # логіка для B1
        await msg.answer("📖 Read the following passage and answer the questions below:\n\n"
                         "⬇️"
                         "In recent years, the popularity of remote work has grown significantly. "
                         "With advances in technology and communication tools, more companies are offering employees the flexibility to work from home or other locations. "
                         "This shift has been driven by several factors, including the desire for a better work-life balance, reduced commuting time, and the ability to attract talent from a broader geographic area.\n\n"
                         "Remote work offers numerous benefits for both employers and employees. "
                         "Employees often report higher job satisfaction, increased productivity, and reduced stress levels. "
                         "Employers can save on office space and related expenses, and they can also access a larger pool of candidates for open positions.\n\n"
                         "However, remote work also presents challenges. "
                         "Some employees may feel isolated or disconnected from their colleagues, which can impact collaboration and team cohesion. "
                         "Additionally, managing remote teams requires different skills and strategies compared to traditional office settings."
                         )
        await msg.answer(
            "✅ Click the 'I read the text' button when you're done.",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text="I read the text")]],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )
        await state.set_state(Survey.read_confirm)

    elif "B2" in msg.text:
        from bot import b2_flow
        await b2_flow.start_b2_flow(msg, state)

    else:
        # Інші рівні — заглушка або просто зберегти
        data = await state.get_data()
        save_to_sheet(data)
        await msg.answer("✅ Дякуємо за твої відповіді!")
        await state.clear()