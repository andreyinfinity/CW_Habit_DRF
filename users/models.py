from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Пользователь"""
    username = None
    email = models.EmailField(verbose_name='e-mail', unique=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    telegram = models.CharField(max_length=50, verbose_name='id telegram', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
