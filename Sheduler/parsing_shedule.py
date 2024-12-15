import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime,timedelta


def parse_shedule_on_week(group:str):
    day = datetime.now()
    current_weekday = day.weekday()
    days_to_monday = (7 - current_weekday) % 7
    monday_date = day + timedelta(days=days_to_monday)
    # Форматируем дату в нужный формат
    formatted_monday = monday_date.strftime('%d.%m.%Y')

    url = f"https://knastu.ru/students/schedule/{group}?form=0&type=0&day={formatted_monday}&simple=0"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='schedule')
    rows = table.find_all('tr', recursive=False)

    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    shedule_on_week = {}

    def extract_lesson_data(cell):
        subject_pattern = re.search(r'<b>(.*?)<\/b>', str(cell), re.DOTALL)
        lecture_pattern = re.search(r'<br\/>(.*?)<br\/>', str(cell), re.DOTALL)
        teacher_pattern = re.search(r'title="Расписание преподавателя">(.*?)<\/a>', str(cell), re.DOTALL)
        room_pattern = re.search(r'<b>(\d+\/\d+)<\/b>', str(cell), re.DOTALL)

        subject = subject_pattern.group(1) if subject_pattern else ""
        lecture_type = lecture_pattern.group(1) if lecture_pattern else ""
        teacher = teacher_pattern.group(1) if teacher_pattern else ""
        room = room_pattern.group(1) if room_pattern else ""

        if not subject and not lecture_type and not teacher and not room:
            return {"Предмет": "-", "Тип занятия": "", "Преподаватель": "", "Аудитория": ""}
        else:
            return {
                "Предмет": subject,
                "Тип занятия": lecture_type,
                "Преподаватель": teacher,
                "Аудитория": room
            }

    for row in rows:
        cells = row.find_all('td')
        for i, cell in enumerate(cells[1:], start=1):
            lesson_info = extract_lesson_data(cell)

            day = days[i - 1]
            if day not in shedule_on_week:
                shedule_on_week[day] = []
            shedule_on_week[day].append(lesson_info)

    return shedule_on_week

