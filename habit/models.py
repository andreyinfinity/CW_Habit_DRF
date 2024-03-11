from django.db import models
from users.models import User


NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """
    Модель привычки.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')
    place_of_execution = models.CharField(max_length=256, verbose_name='место выполнения', **NULLABLE)
    action = models.TextField(verbose_name='действие')
    time_of_execution = models.DateTimeField(verbose_name='время начала выполнения', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='длительность выполнения в секундах', **NULLABLE)
    periodicity_in_days = models.PositiveIntegerField(verbose_name='периодичность в днях')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    award = models.CharField(max_length=256, verbose_name='вознаграждение', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки')
    is_public = models.BooleanField(verbose_name='признак публичности')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ['action']

    def __str__(self):
        return f'{self.action}'
