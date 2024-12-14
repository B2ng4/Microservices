

from bd_functions import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


years = get_unique_years()

year_buttons = [KeyboardButton(text=str(year),callback_data=f"year_{year}") for year in years]



keyboard_years = ReplyKeyboardMarkup(
    keyboard=[year_buttons],
    resize_keyboard=True
)
