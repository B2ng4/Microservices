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
    await msg.answer("Привет! Я твой помощник в КнАГУ.  Ты можешь ко мне обращаться когда нужно, я помогу тебе подготовиться к сессии, автоматически отправляю расписание и многое другое....")
    await msg.answer("Давай зарегистрируемся! Для начала, выбери год поступления в ВУЗ", reply_markup=keyboard_years)


@router.callback_query(lambda c: c.data and c.data.startswith('year_'))
async def process_year_callback(callback_query: CallbackQuery):
    year = callback_query.data.split('_')[1]
    groups = get_groups(year)
    keyboard_groups = create_groups_keyboard(groups)
    await callback_query.message.edit_text(
        text="Отлично! А теперь выбери свою группу",
        reply_markup=keyboard_groups
    )


@router.callback_query(lambda c: c.data and c.data.startswith('group_'))
async def process_year_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = str(callback_query.from_user.id)
    name = str(callback_query.from_user.first_name)
    group = str(callback_query.data.split('_')[1])
    group_uuid = str(get_uuid_group(group))
    if register(user_id,name,group_uuid):
        await callback_query.message.edit_text(
            text="Отлично! Вы успешно зарегистрированы!",
            reply_markup=keyboard_years
        )






