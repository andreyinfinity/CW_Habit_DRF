from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from habit.models import Habit
"""
Валидаторы
+ Исключить одновременный выбор связанной привычки и указания вознаграждения.
+ В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.
+ Время выполнения должно быть не больше 120 секунд.
+ В связанные привычки могут попадать только привычки с признаком приятной привычки.
+ У приятной привычки не может быть вознаграждения или связанной привычки.
+ Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз.
"""


def max_time(value):
    """Максимальное время выполнения привычки в секундах"""
    if value > 120:
        raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд")


def max_periodicity(value):
    """Максимальная периодичность привычки"""
    if value > 7:
        raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")


def validate_pleasant_habit(related_habit, award):
    """Валидация приятной привычки. Она не должна ссылаться на привычку и иметь вознаграждение"""
    if related_habit is not None or award is not None:
        raise serializers.ValidationError(
            "Приятная привычка не должна иметь ни связанной привычки, не вознаграждения"
        )


def validate_useful_habit(related_habit, award):
    """Валидация полезной привычки."""
    if not related_habit and not award:
        raise serializers.ValidationError(
            "Полезная привычка должна иметь либо связанную привычку, либо вознаграждение"
        )
    elif related_habit and award:
        raise serializers.ValidationError(
            "Полезная привычка должна иметь либо только связанную привычку, либо только вознаграждение"
        )
    elif related_habit and not award:
        habit = get_object_or_404(Habit, pk=related_habit.pk)
        # Если связанная привычка полезная
        if not habit.is_pleasant:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки"
            )
