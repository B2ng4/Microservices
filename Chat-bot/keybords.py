from tokenize import group

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bd_functions import get_unique_years  #

years = get_unique_years()
year_buttons = [InlineKeyboardButton(text=str(year), callback_data=f"year_{year}") for year in years]
keyboard_years = InlineKeyboardMarkup(inline_keyboard=[year_buttons])



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