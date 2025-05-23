from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🚀 Почати опитування")]],
    resize_keyboard=True
)

interest_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Граматика")],
        [KeyboardButton(text="Розмовна мова")],
        [KeyboardButton(text="Бізнес-англійська")],
        [KeyboardButton(text="Підготовка до іспитів")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

format_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Індивідуальні заняття")],
        [KeyboardButton(text="Групові заняття")],
        [KeyboardButton(text="Заняття в парі")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pace_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="2 рази на тиждень")],
        [KeyboardButton(text="3 рази на тиждень")],
        [KeyboardButton(text="1 раз на тиждень")],
        [KeyboardButton(text="Мікро-навчання")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

level_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A1: Beginner + Elementary (Початковий)")],
        [KeyboardButton(text="A2: Pre-Intermediate (Нижчий за середній)")],
        [KeyboardButton(text="B1: Intermediate (Середній)")],
        [KeyboardButton(text="B2: Upper-Intermediate (Вище за середній)")],
        [KeyboardButton(text="C1: Advanced (Просунутий)")],
        [KeyboardButton(text="C2: Proficient (Досконалий)")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# --- Reading Questions Q1 ---
reading_q1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Advances in technology and communication tools")],
        [KeyboardButton(text="B) Increased office space")],
        [KeyboardButton(text="C) Reduced work-life balance")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reading_q2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Higher commuting costs and stress levels")],
        [KeyboardButton(text="B) Higher job satisfaction and increased productivity")],
        [KeyboardButton(text="C) More office space and expenses")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reading_q3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Due to increased team cohesion")],
        [KeyboardButton(text="B) Due to reduced work-life balance")],
        [KeyboardButton(text="C) Due to a lack of connection with colleagues")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reading_q4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Traditional office settings")],
        [KeyboardButton(text="B) The right technology and clear policies")],
        [KeyboardButton(text="C) Increased commuting time")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# --- Grammar Questions ---
grammar_q1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will offer")],
        [KeyboardButton(text="B) will have offered")],
        [KeyboardButton(text="C) will be offering")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

grammar_q2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) uses")],
        [KeyboardButton(text="B) use")],
        [KeyboardButton(text="C) used")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

grammar_q3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will implement")],
        [KeyboardButton(text="B) will be implementing")],
        [KeyboardButton(text="C) will have implemented")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

grammar_q4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will invest")],
        [KeyboardButton(text="B) will be investing")],
        [KeyboardButton(text="C) will have invested")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

grammar_q5_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Do, work")],
        [KeyboardButton(text="B) Have, worked")],
        [KeyboardButton(text="C) Will, work")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


# --- Reading Questions Q1 ---

b2_read_confirm_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="I read the text")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_q1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Large changes lead to remarkable results")],
        [KeyboardButton(text="B) Tiny changes can lead to remarkable results")],
        [KeyboardButton(text="C) Habits are difficult to change")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_q2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Linking new habits to existing ones")],
        [KeyboardButton(text="B) Focusing on achieving specific outcomes")],
        [KeyboardButton(text="C) Making habits difficult to adopt")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_q3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Because it focuses on specific goals")],
        [KeyboardButton(text="B) Because it involves becoming the type of person you want to be")],
        [KeyboardButton(text="C) Because it makes habits less attractive")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_q4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Make it obvious")],
        [KeyboardButton(text="B) Make it complex")],
        [KeyboardButton(text="C) Make it satisfying")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_q5_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) To achieve short-term goals")],
        [KeyboardButton(text="B) To transform habits and achieve long-term goals")],
        [KeyboardButton(text="C) To make habits more challenging")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_essay_topic_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Why is diligence important in maintaining good habits?")],
        [KeyboardButton(text="How does positive reinforcement help solidify new habits?")],
        [KeyboardButton(text="What role does the subconscious mind play in habit formation?")],
        [KeyboardButton(text="Why is resilience important in maintaining habits?")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_g1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will develop")],
        [KeyboardButton(text="B) will have developed")],
        [KeyboardButton(text="C) will be developing")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_g2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) uses")],
        [KeyboardButton(text="B) use")],
        [KeyboardButton(text="C) used")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_g3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will adopt")],
        [KeyboardButton(text="B) will be adopting")],
        [KeyboardButton(text="C) will have adopted")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_g4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) will introduce")],
        [KeyboardButton(text="B) will be introducing")],
        [KeyboardButton(text="C) will have introduced")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

b2_g5_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="A) Do, read")],
        [KeyboardButton(text="B) Have, read")],
        [KeyboardButton(text="C) Will, read")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

#Pre A1

pre_a1_read_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Текст прочитано")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) Japan"), KeyboardButton(text="b) Spain")],
        [KeyboardButton(text="c) Italy"), KeyboardButton(text="d) French")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) do"), KeyboardButton(text="b) does")],
        [KeyboardButton(text="c) don't"), KeyboardButton(text="d) doesn't")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) Do"), KeyboardButton(text="b) Does")],
        [KeyboardButton(text="c) Is"), KeyboardButton(text="d) Don’t")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) is he"), KeyboardButton(text="b) he’s")],
        [KeyboardButton(text="c) do he"), KeyboardButton(text="d) does he")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g5_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) watch"), KeyboardButton(text="b) watching")],
        [KeyboardButton(text="c) watches"), KeyboardButton(text="d) to watching")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g6_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) to"), KeyboardButton(text="b) at")],
        [KeyboardButton(text="c) -"), KeyboardButton(text="d) the")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g7_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) brother’s"), KeyboardButton(text="b) sister is")],
        [KeyboardButton(text="c) brother"), KeyboardButton(text="d) sisters")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g8_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) never is"), KeyboardButton(text="b) ’s often")],
        [KeyboardButton(text="c) often is"), KeyboardButton(text="d) never")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g9_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) some"), KeyboardButton(text="b) any")],
        [KeyboardButton(text="c) the"), KeyboardButton(text="d) a")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pre_a1_g10_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="a) at"), KeyboardButton(text="b) the")],
        [KeyboardButton(text="c) on"), KeyboardButton(text="d) in")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


#A1


a1_q1_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) He stays at home."),
               KeyboardButton(text="B) He goes jogging."),
               KeyboardButton(text="C) He meets his friends.")]],
    resize_keyboard=True
)

a1_q2_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) At home"),
               KeyboardButton(text="B) At a café"),
               KeyboardButton(text="C) At a restaurant")]],
    resize_keyboard=True
)

a1_q3_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) He works at school."),
               KeyboardButton(text="B) He visits friends or goes to the cinema."),
               KeyboardButton(text="C) He studies at the library.")]],
    resize_keyboard=True
)

a1_q4_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) He travels to another city."),
               KeyboardButton(text="B) He cleans his apartment and reads books."),
               KeyboardButton(text="C) He plays football with his friends.")]],
    resize_keyboard=True
)

a1_q5_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) He goes jogging."),
               KeyboardButton(text="B) He listens to music or watches TV."),
               KeyboardButton(text="C) He visits his family.")]],
    resize_keyboard=True
)

a1_g1_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) go"),
               KeyboardButton(text="B) goes"),
               KeyboardButton(text="C) going")]],
    resize_keyboard=True
)

a1_g2_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) go"),
               KeyboardButton(text="B) went"),
               KeyboardButton(text="C) goes")]],
    resize_keyboard=True
)

a1_g3_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) Did"),
               KeyboardButton(text="B) Have"),
               KeyboardButton(text="C) Do")]],
    resize_keyboard=True
)

a1_g4_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) rain"),
               KeyboardButton(text="B) rains"),
               KeyboardButton(text="C) will rain")]],
    resize_keyboard=True
)

a1_g5_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="A) eat"),
               KeyboardButton(text="B) were eating"),
               KeyboardButton(text="C) ate")]],
    resize_keyboard=True
)