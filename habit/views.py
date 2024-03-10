from rest_framework import generics
from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer


class HabitListCreate(generics.ListCreateAPIView):
    """Create and Listview привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        """Добавление поля пользователя"""
        serializer.save(user=self.request.user)


class HabitRUD(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update, Destroy привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

