from datetime import datetime, timezone, timedelta
from celery import shared_task
from django.db.models import F
from habit.models import Habit
from habit.services import send_telegram_message


@shared_task
def send_notification():
    """Функция отправки уведомлений пользователям"""
    current_time = datetime.now(timezone.utc)
    # получение всех полезных привычек, у которых время начала выполнения меньше либо равно текущему
    habits = Habit.objects.all().filter(time_of_execution__lte=current_time, is_pleasant=False)
    if habits:
        for habit in habits:
            send_telegram_message(habit)
            habit.time_of_execution = F('time_of_execution') + timedelta(days=habit.periodicity_in_days)
            habit.save()
