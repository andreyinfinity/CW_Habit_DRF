from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from users.models import User


class UserTestCase(APITestCase):
    """Тестирование CRUD пользователя"""
    def setUp(self):
        self.client = APIClient()
        # Создание тестового пользователя
        self.user = User.objects.create(email='test@test.ru', password='test')
        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Тест регистрации пользователя"""
        # Эндпойнт регистрации пользователя
        url = reverse('user:register')
        data = {
            "email": "test_create@test.com",
            "password": "test",
        }

        response = self.client.post(path=url, data=data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверка ответа
        self.assertEqual(
            response.json()["email"],
            "test_create@test.com"
        )

    def test_retrieve_user(self):
        """Тест просмотра профиля пользователя"""
        # Эндпойнт просмотра профиля
        url = reverse('user:profile')

        response = self.client.get(path=url)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка ответа
        self.assertEqual(
            response.json()["email"],
            "test@test.ru"
        )

    def test_patch_user(self):
        """Тест редактирования профиля пользователя"""
        # Эндпойнт редактирования профиля
        url = reverse('user:profile')

        response = self.client.patch(path=url, data={'first_name': 'Test name'})
        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка ответа
        self.assertEqual(
            response.json()['first_name'],
            "Test name"
        )

    def test_destroy_user(self):
        """Тест удаления пользователя"""
        # Эндпойнт удаления пользователя
        url = reverse('user:profile')
        response = self.client.delete(path=url)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Проверка, что пользователь деактивирован
        self.assertFalse(User.objects.get(pk=self.user.pk).is_active)
