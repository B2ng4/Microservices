from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from bd_functions import *
from api_Requests.reg import register
from api_Requests.get_shedule import shedule
from add_data import *
from keybords import *

router = Router()



@router.message(Command("start"))
async def start_handler(msg: Message):
    """Начать"""
    user_id = str(msg.from_user.id)
    if not(check_user_exists(user_id)):
        keyboard_years = create_years_keyboard()
        await msg.answer("Привет! Я твой помощник в КнАГУ.  Ты можешь ко мне обращаться когда нужно, я помогу тебе подготовиться к сессии, автоматически отправляю расписание и многое другое....")
        await msg.answer("Давай зарегистрируемся! Для начала, выбери год поступления в ВУЗ", reply_markup=keyboard_years)
    else:
        func_keyboard = create_functions_keyboard()
        name = str(msg.from_user.first_name)
        await msg.answer(f"Привет, {name}" , reply_markup=func_keyboard)




@router.callback_query(lambda c: c.data and c.data.startswith('year_'))
async def process_year_callback(callback_query: CallbackQuery):
    """Выбираем год начала обучения"""
    year = callback_query.data.split('_')[1]
    groups = get_groups(year)
    keyboard_groups = create_groups_keyboard(groups)
    await callback_query.message.edit_text(
        text="Отлично! А теперь выбери свою группу",
        reply_markup=keyboard_groups
    )


@router.callback_query(lambda c: c.data and c.data.startswith('group_'))
async def process_year_callback(callback_query: CallbackQuery):
    """Выбираем группу"""
    user_id = str(callback_query.from_user.id)
    name = str(callback_query.from_user.first_name)
    group = str(callback_query.data.split('_')[1])
    group_uuid = str(get_uuid_group(group)) #Получаем первое значение
    keyboard_func = create_functions_keyboard() # Теперь используем обычную клавиатуру
    if register(user_id, name, group_uuid):
        await callback_query.message.edit_text(
            text="Отлично! Вы успешно зарегистрированы!"
        )
        await callback_query.message.answer(
            text="Выберите действие:",
            reply_markup=keyboard_func
        )
        await callback_query.answer()
    else:
        await callback_query.message.answer(
            text="Вы уже зарегистрированы!"
        )
        await callback_query.answer()


@router.message(lambda message: message.text == "Получить расписание 📅")
async def request_text(message: Message):
    group_uuid = get_user_uuid_group (str(message.from_user.id))
    schedule = shedule(group_uuid)
    for day, lessons in schedule.items():
        text = f"<b> Расписание на  ({day})</b>\n\n"
        for i, lesson in enumerate(lessons, 1):
            if lesson['Предмет'] == "-":
                continue
            else:
                text += f"    <i>{digits[i - 1]} {pair_times[i - 1]}.\n    <b>{lesson['Предмет']}</b>: {lesson['Тип занятия']}</i>\n"
                text += f"    <i>Преподаватель: {lesson['Преподаватель']}</i>\n"
                text += f"    <i>Аудитория: {lesson['Аудитория']}</i>\n\n"

        await message.answer(text=text, parse_mode="HTML")
        break
