from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from bd_functions import *
from api_Requests.reg import register
from api_Requests.get_shedule import shedule
from api_Requests.get_lessons import lessons
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


@router.message(lambda message: message.text == "расписание на неделю 📅")
async def show_week_schedule(message: Message):
    group_uuid = get_user_uuid_group(str(message.from_user.id))
    schedule = shedule(group_uuid)

    keyboard = shedule_keyboard(schedule)
    await message.answer(
        text="Выберите день недели, чтобы увидеть расписание:",
        reply_markup=keyboard.as_markup()
    )


@router.callback_query(lambda c: c.data and c.data.startswith('schedule_'))
async def show_day_schedule(callback_query: CallbackQuery):
    group_uuid = get_user_uuid_group(str(callback_query.from_user.id))
    schedule = shedule(group_uuid)
    day = callback_query.data.split('_')[1]

    if day not in schedule:
        await callback_query.answer("Расписание для этого дня не найдено!", show_alert=True)
        return

    lessons = schedule[day]
    text = f"<b>Расписание на {day}:</b>\n\n"
    if not lessons:
        text += "  <i>Нет занятий</i>\n"
    else:
        for i, lesson in enumerate(lessons, 1):
            if lesson['Предмет'] == "-":
                continue
            text += f"    <i>{digits[i - 1]} {pair_times[i - 1]}.\n    <b>{lesson['Предмет']}</b>: {lesson['Тип занятия']}</i>\n"
            text += f"    <i>Преподаватель: {lesson['Преподаватель']}</i>\n"
            text += f"    <i>Аудитория: {lesson['Аудитория']}</i>\n\n"

    await callback_query.message.edit_text(
        text=text,
        parse_mode="HTML",
        reply_markup=callback_query.message.reply_markup
    )
    await callback_query.answer()


@router.message(lambda message: message.text == "Авто-расписание ⌚️")
async def set_auto_shedule(message: Message):
    keyboard_auto = create_auto_keyboard()
    await message.answer("<b>Настройка автоматической отправки расписания</b> \n Если включить, бот будет отправлять расписание на день в 6 утра", reply_markup=keyboard_auto)


@router.callback_query(lambda c: c.data == "auto_on")
async def enable_auto_schedule(callback_query: CallbackQuery):
    func_keyboard = create_functions_keyboard()
    await callback_query.message.edit_text(
        "<b>Авто-расписание включено ✅</b>\n\n"
        "Бот будет автоматически отправлять расписание каждый день в 6 утра.\n"
        "Вы можете отключить эту функцию в любое время.",
        parse_mode="HTML"
    )
    await callback_query.answer("Авто-расписание включено!")



@router.message(lambda message: message.text == "Рекомендации на текущую сессию 🔑")
async def set_disciplines(message: Message):
    disciplins = lessons(str(message.from_user.id))
    discipline_list = disciplins[0]["Дисциплины"]

    disc_keyboard = create_disciplins_keyboard(discipline_list)

    await message.answer(
        text="Выбери предмет, по которому у тебя возникают проблемы",
        reply_markup=disc_keyboard
    )

@router.callback_query(lambda c: c.data and c.data.startswith('dis_'))
async def get_subject(callback_query: CallbackQuery):
    discioline = callback_query.data.split('_')[1]
    recomend_keyboard = create_recomendation_keyboard()
    await callback_query.message.edit_text(f"Выбран предмет: {discioline}",parse_mode="HTML", reply_markup=recomend_keyboard)




