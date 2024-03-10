from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек"""
    def setUp(self):
        self.client = APIClient()
        # Создание тестового пользователя
        self.user = User.objects.create(email='test@test.ru', password='test')
        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)
        # Создание тестовой привычки в БД
        data = {
            'action': '10 отжиманий',
            'award': 'мороженка',
            'is_pleasant': False,
            'is_public': False,
            'periodicity_in_days': 1,
            'place_of_execution': 'дом',
            'related_habit': None,
            'time_of_execution': '2024-03-10T00:00:00Z',
            'time_to_complete': 120,
            'user': self.user
            }
        self.habit = Habit.objects.create(**data)

    def test_create_habit(self):
        """Тест создания привычки"""
        # Эндпойнт создания привычки
        url = reverse('habit:habit-list')
        data = {
            "time_to_complete": 120,
            "periodicity_in_days": 1,
            "place_of_execution": "дом",
            "action": "10 отжиманий",
            "time_of_execution": "2024-03-10 00:00",
            "award": "мороженка",
            "is_pleasant": False,
            "is_public": False,
        }

        response = self.client.post(path=url, data=data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверка ответа
        self.assertEqual(
            response.json(),
            {
                'action': '10 отжиманий',
                'award': 'мороженка',
                'id': self.habit.pk + 1,
                'is_pleasant': False,
                'is_public': False,
                'periodicity_in_days': 1,
                'place_of_execution': 'дом',
                'related_habit': None,
                'time_of_execution': '2024-03-10T00:00:00Z',
                'time_to_complete': 120,
                'user': self.user.pk
            }
        )

    def test_list_habit(self):
        """Тест списка привычек"""
        # Эндпойнт списка привычек
        url = reverse('habit:habit-list')
        response = self.client.get(path=url)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка ответа
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [{
                    'action': '10 отжиманий',
                    'award': 'мороженка',
                    'id': self.habit.pk,
                    'is_pleasant': False,
                    'is_public': False,
                    'periodicity_in_days': 1,
                    'place_of_execution': 'дом',
                    'related_habit': None,
                    'time_of_execution': '2024-03-10T00:00:00Z',
                    'time_to_complete': 120,
                    'user': self.user.pk
                }]}
        )

    def test_retrieve_habit(self):
        """Тест просмотра привычки"""
        # Эндпойнт просмотра привычки
        url = reverse('habit:habit', args=[self.habit.pk])

        response = self.client.get(path=url)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка ответа
        self.assertEqual(
            response.json(),
            {
                'action': '10 отжиманий',
                'award': 'мороженка',
                'id': self.habit.pk,
                'is_pleasant': False,
                'is_public': False,
                'periodicity_in_days': 1,
                'place_of_execution': 'дом',
                'related_habit': None,
                'time_of_execution': '2024-03-10T00:00:00Z',
                'time_to_complete': 120,
                'user': self.user.pk
            }
        )

    def test_patch_habit(self):
        """Тест редактирования привычки"""
        # Эндпойнт редактирования привычки
        url = reverse('habit:habit', args=[self.habit.pk])

        response = self.client.patch(path=url, data={'action': '10 приседаний'})
        print(response.json())
        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка ответа
        self.assertEqual(
            response.json(),
            {
                'action': '10 приседаний',
                'award': 'мороженка',
                'id': self.habit.pk,
                'is_pleasant': False,
                'is_public': False,
                'periodicity_in_days': 1,
                'place_of_execution': 'дом',
                'related_habit': None,
                'time_of_execution': '2024-03-10T00:00:00Z',
                'time_to_complete': 120,
                'user': self.user.pk
            }
        )

    def test_destroy_habit(self):
        """Тест удаления привычки"""
        # Эндпойнт удаления привычки
        url = reverse('habit:habit', args=[self.habit.pk])

        response = self.client.delete(path=url)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
