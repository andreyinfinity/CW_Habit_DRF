import requests
from config.settings import TELEGRAM_API_KEY


telegram_token = TELEGRAM_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit):
    """Функция отправки сообщения в телеграм"""

    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram,
            'text': message
        })


def create_message(habit, user):
    """Функция создания сообщения"""
    if habit.award:
        award = f"После ты получишь {habit.award}!"
    elif habit.related_habit:
        award = f"После надо {habit.related_habit.action}!"
    else:
        return "Привет"
    message = (f"Привет, {user}! "
               f"Сегодня в {habit.time_of_execution.strftime('%H:%M')} "
               f"в {habit.place_of_execution} "
               f"тебе надо выполнить {habit.action} "
               f"в течении {habit.time_to_complete} секунд. "
               f"{award}")
    return message
