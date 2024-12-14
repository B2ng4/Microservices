from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,FSInputFile
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

from aiogram import  types, F

from keybords import *
import os

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я твой помощник в КнАГУ.  Ты можешь ко мне обращаться когда нужно, я помогу тебе подготовиться к сессии, автоматически отправляю расписание и многое другое....")
    await msg.answer("Давай зарегистрируемся! Для начала, выбери год поступления в ВУЗ", reply_markup=keyboard_years)


