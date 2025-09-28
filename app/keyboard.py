from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Положение")],
    [KeyboardButton(text="Принять участие")],
    [KeyboardButton(text="Часто задаваемые вопросы"),
    KeyboardButton(text="Зрительские билеты"),
    KeyboardButton(text="Соц.сети")]
],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню")


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Положение из Google Диска', url='https://docs.google.com/document/d/1zBISomctaBCs4cyqgL-dUMFMVa-H4rlW/edit?usp=drive_link&ouid=104578914159576960790&rtpof=true&sd=true')]
])


aredl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажмите чтобы получить 100$', url='https://aredl.net/list/114283297?list=classic&search=')]
])


social_network = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK', url='https://vk.com/flatwhite11'), InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/flat_.white?igsh=MXd0bHRqeTM2NXVlNw==')]
])

question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Не получил/a сообщение о прохождении ресторации ?", callback_data="faq_1")],
    [InlineKeyboardButton(text="Реквизит в номере ?", callback_data="faq_2")],
    [InlineKeyboardButton(text="Замена фонограммы ?", callback_data="faq_3")],
    [InlineKeyboardButton(text="Какой тайминг мероприятия?", callback_data="faq_4")],
    [InlineKeyboardButton(text="Нужен входной билет для тренера/руководителя команды?", callback_data="faq_5")],
    [InlineKeyboardButton(text="Другой вопрос?", callback_data="faq_6")],
])
