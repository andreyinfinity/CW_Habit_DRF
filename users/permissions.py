from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    """Проверка является ли пользователь сам собой"""
    message = 'Доступ разрешен только к своему профилю'

    def has_object_permission(self, request, view, obj):
        return request.user == obj
