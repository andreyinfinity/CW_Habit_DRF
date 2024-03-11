from rest_framework import serializers
from habit.models import Habit
from habit.validators import max_time, max_periodicity, validate_pleasant_habit, validate_useful_habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычки"""
    time_to_complete = serializers.IntegerField(validators=[max_time])
    periodicity_in_days = serializers.IntegerField(validators=[max_periodicity])

    def validate(self, attrs):
        """Валидация группы полей"""
        related_habit = attrs.get('related_habit', None)
        award = attrs.get('award', None)
        is_pleasant = attrs.get('is_pleasant')
        # Если привычка приятная
        if is_pleasant:
            validate_pleasant_habit(related_habit, award)
        # Иначе если привычка полезная
        else:
            validate_useful_habit(related_habit, award)
            if not attrs.get("place_of_execution"):
                raise serializers.ValidationError("поле 'place_of_execution' не может быть пустым")
            if not attrs.get("time_of_execution"):
                raise serializers.ValidationError("поле 'time_of_execution' не может быть пустым")
        return attrs

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user']
