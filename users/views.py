from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UserRegister(generics.CreateAPIView):
    """Контроллер регистрации пользователя, доступен для всех пользователей"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Хеширование пароля перед записью в БД"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    """CRUD для работы с профилем пользователя"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """Получение самого себя в качестве объекта пользователя"""
        return User.objects.get(pk=self.request.user.pk)

    def perform_update(self, serializer):
        """Хеширование пароля при обновлении профиля"""
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def perform_destroy(self, instance):
        """При удалении пользователя происходит его деактивация"""
        user = instance
        user.is_active = False
        user.save()
