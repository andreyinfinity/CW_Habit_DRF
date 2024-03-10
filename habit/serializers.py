from rest_framework import serializers
from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user']
