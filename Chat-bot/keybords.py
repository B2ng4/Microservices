from tokenize import group

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from bd_functions import get_unique_years  #


def create_years_keyboard():
    years = get_unique_years()
    year_buttons = [InlineKeyboardButton(text=str(year), callback_data=f"year_{year}") for year in years]
    return InlineKeyboardMarkup(inline_keyboard=[year_buttons])



def create_groups_keyboard(groups, buttons_per_row=3):
    keyboard_groups = []
    row = []
    for group in groups:
        row.append(InlineKeyboardButton(text=str(group), callback_data=f"group_{group}"))
        if len(row) == buttons_per_row:
            keyboard_groups.append(row)
            row = []
    if row:
        keyboard_groups.append(row)
    return InlineKeyboardMarkup(inline_keyboard=keyboard_groups)


def create_functions_keyboard():
    btn1 = KeyboardButton(text='расписание на неделю 📅')
    btn2 = KeyboardButton(text='Авто-расписание ⌚️')
    btn3 = KeyboardButton(text='Рекомендации на текущую сессию 🔑')

    return ReplyKeyboardMarkup(
        keyboard=[[btn1], [btn2], [btn3]],
        resize_keyboard=True
    )

def shedule_keyboard(schedule):
    keyboard = InlineKeyboardBuilder()

    for day in schedule.keys():
        keyboard.button(text=day, callback_data=f"schedule_{day}")


    keyboard.adjust(2)
    return keyboard

def create_auto_keyboard():
    btn1 = InlineKeyboardButton(text="Включить", callback_data="auto_on")
    return InlineKeyboardMarkup(inline_keyboard=[[btn1]])


def create_disciplins_keyboard(disciplins):
    disc_buttons = [
        InlineKeyboardButton(
            text="📍"+disciplin,
            callback_data=f"dis_{i}"
        )
        for i, disciplin in enumerate(disciplins)
    ]

    return InlineKeyboardMarkup(inline_keyboard=[[button] for button in disc_buttons])