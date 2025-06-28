from rest_framework.test import APITestCase
from habits.serializers import HabitSerializer
from users.models import User


class HabitSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='pass123')
        self.valid_data = {
            'action': 'Зарядка',
            'place': 'Дом',
            'time': '07:00:00',
            'frequency': 1,
            'duration': 90
        }

    def test_valid_serializer_data(self):
        """Тест валидных данных"""
        serializer = HabitSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        habit = serializer.save(user=self.user)
        self.assertEqual(habit.action, 'Зарядка')

    def test_invalid_duration(self):
        """Тест слишком большой длительности"""
        invalid_data = self.valid_data.copy()
        invalid_data['duration'] = 121
        serializer = HabitSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('duration', serializer.errors)

    def test_pleasant_with_reward(self):
        """Приятная привычка с вознаграждением должна быть невалидной"""
        invalid_data = self.valid_data.copy()
        invalid_data.update({
            'is_pleasant': True,
            'reward': 'Кофе'
        })
        serializer = HabitSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
