from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListCreate(generics.ListCreateAPIView):
    """Create and Listview привычек"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Добавление поля пользователя"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Отображение только своих привычек"""
        return Habit.objects.filter(user=self.request.user)


class HabitRUD(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update, Destroy привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitList(generics.ListAPIView):
    """Список публичных привычек"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Отображение только публичных привычек"""
        return Habit.objects.filter(is_public=True)
