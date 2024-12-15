from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from bd_functions import *
from api_Requests.reg import register
from keybords import *

router = Router()



@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    """Начать"""
    user_id = str(msg.from_user.id)
    if not(check_user_exists(user_id)):
        keyboard_years = create_years_keyboard()
        await msg.answer("Привет! Я твой помощник в КнАГУ.  Ты можешь ко мне обращаться когда нужно, я помогу тебе подготовиться к сессии, автоматически отправляю расписание и многое другое....")
        await msg.answer("Давай зарегистрируемся! Для начала, выбери год поступления в ВУЗ", reply_markup=keyboard_years)
    else:
        func_keyboard = create_functions_keyboard()
        await msg.answer("Привет! Ты уже зарегистрирован", reply_markup=func_keyboard)


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
async def process_year_callback(callback_query: CallbackQuery, state: FSMContext):
    """Выбираем группу"""
    user_id = str(callback_query.from_user.id)
    name = str(callback_query.from_user.first_name)
    group = str(callback_query.data.split('_')[1])
    group_uuid = str(get_uuid_group(group)[0]) #Получаем первое значение
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






