from tokenize import group

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
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
    btn1 = KeyboardButton(text='Получить расписание 📅')
    btn2 = KeyboardButton(text='Рекомендации на текущую сессию 🔑')

    return ReplyKeyboardMarkup(
        keyboard=[[btn1, btn2]],
        resize_keyboard=True
    )
