from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import app.keyboard as kb


#Класс состояний "Для регистрации"
class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_command_name = State()
    waiting_for_members = State()
    waiting_for_nomination = State()
    waiting_for_link = State()


router = Router()

# Обработчики
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Приветствуем всех танцоров и зрителей!\n'
        'Мы рады сообщить, что регистрация на FLAT WHITE CHAMP открыта!\n'
        'Встречаемся 25.05.25 в клубе A2.\n'
        'Вся необходимая информация - в положении.\n'
        'Пусть этот чемпионат станет площадкой для самовыражения и ярких эмоций.\n'
        'Удачи всем, сделаем этот день незабываемым!\n'
        'FLAT WHITE CHAMP',
    reply_markup=kb.main)


@router.message(F.text == "Принять участие")
async def start_registration(message: Message, state: FSMContext):
    await state.set_state(Registration.waiting_for_name)
    await message.answer(
        "ФИО руководителя/солиста:",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Registration.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.waiting_for_phone)
    await message.answer("Номер телефона руководителя/солиста:")


@router.message(Registration.waiting_for_phone)
async def process_command_name(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Registration.waiting_for_command_name)
    await message.answer("Название команды: ")


@router.message(Registration.waiting_for_command_name)
async def process_command_name(message: Message, state: FSMContext):
    await state.update_data(command_name=message.text)
    await state.set_state(Registration.waiting_for_members)
    await message.answer("Количество участников:")


@router.message(Registration.waiting_for_members)
async def process_members(message: Message, state: FSMContext):
    await state.update_data(members=message.text)
    await state.set_state(Registration.waiting_for_nomination)
    await message.answer("Номинация (указать название номинации):")


@router.message(Registration.waiting_for_nomination)
async def process_nomination(message: Message, state: FSMContext):
    await state.update_data(nomination=message.text)
    await state.set_state(Registration.waiting_for_link)
    await message.answer("Ссылка для видеоотбора:")


@router.message(Registration.waiting_for_link)
async def process_link(message: Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()

    await state.clear()

    registration_text = (
        "🎉 НОВАЯ ЗАЯВКА НА УЧАСТИЕ\n\n"
            f"👤 ФИО: {user_data['name']}\n"
            f"📞 Телефон: {user_data['phone']}\n"
            f"🏆 Команда: {user_data['command_name']}\n"
            f"👥 Участников: {user_data['members']}\n"
            f"🎯 Номинация: {user_data['nomination']}\n"
            f"📺 Ссылка: {message.text}\n\n"
    )

    CHANNEL_ID = "@ratatyiii314"

    print(f"Пытаюсь отправить в канал {CHANNEL_ID}")
    await bot.send_message(chat_id=CHANNEL_ID, text=registration_text)
    await message.answer("✅ Заявка отправлена!", reply_markup=kb.main)
    print("Сообщение отправлено успешно!")


@router.message(F.text == "Положение")
async def handle_position(message: Message):
    await message.answer(
        text="Открыть положение:",
        reply_markup=kb.settings
    )


@router.message(F.text == "Принять участие")
async def registration(message: Message, state: FSMContext):
    await state.set_state(Registration.waiting_for_name)


@router.message(F.text == "Соц.сети")
async def network_button(message: Message):
    await message.answer(
        text="Наши соц. сети",
        reply_markup=kb.social_network
    )


@router.message(F.text == "Зрительские билеты")
async def aredl_link(message: Message):
    await message.answer(
        text="Купить зрительский билет: ",
        reply_markup=kb.aredl
    )


@router.message(F.text == "Часто задаваемые вопросы")
async def questions(message: Message):
    await message.answer(
        text='Выберите вопрос: ',
        reply_markup=kb.question
    )


#Обработчик ответов на часто задаваемые вопросы
@router.callback_query(F.data.startswith("faq_"))
async def handle_faq(callback: CallbackQuery):
    faq_number = callback.data.split("_")[1]

    #Ответы на вопросы
    answer = {
        "1": "В положении указано, за какой срок поступит сообщение о прохождении регистрации (ссылка). Если срок истек, напиши нашему Админу FW CHAMP (@MARIVANNA_1)",
        "2": "Подробно расскажи нашему админу FW CHAMP (@MARIVANNA_1)",
        "3": "Отправь на мою почту новую фонограмму с темой письма (согласно положения) и допиши <ЗАМЕНА>",
        "4": "Точный тайминг выложим 20.05.25 в FLAT WHITE CHAMP (ссылка на тг канал), подпишись и следи за инфекцией (какой нахуй инфекцией, где ссылка на тгк ебанаты)",
        "5": "Входной билет не нужен. Вход бесплатный",
        "6": "Наш администратор мероприятия поможет вам. Админ FW CHAMP (@MARIVANNA_1)"
    }

    await callback.message.edit_text(
        text=answer[faq_number],
        reply_markup=kb.question
    )


# Обработка некомандных сообщений
@router.message(F.text)
async def any_message_handler(message: Message):
    await message.answer("Мы тебя немного не понимаем, воспользуйся командами")