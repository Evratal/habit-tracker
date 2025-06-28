from django.test import TestCase
from django.core.exceptions import ValidationError
from users.models import User
from ..models import Habit
import datetime


class HabitModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.pleasant_habit = Habit.objects.create(
            user=self.user,
            action="Медитация",
            place="Гостиная",
            time=datetime.time(8, 0),
            is_pleasant=True,
            duration=300,
            is_public=True
        )

    def test_habit_creation(self):
        """Тест создания привычки с валидными данными"""
        habit = Habit.objects.create(
            user=self.user,
            action="Чтение",
            place="Кровать",
            time=datetime.time(22, 0),
            frequency=7,
            duration=120
        )
        self.assertEqual(habit.action, "Чтение")
        self.assertEqual(habit.frequency, 7)
        self.assertFalse(habit.is_pleasant)

    def test_pleasant_habit_constraints(self):
        """Приятная привычка не должна иметь вознаграждения или связанной привычки"""
        with self.assertRaises(ValidationError):
            habit = Habit(
                user=self.user,
                action="Прослушивание музыки",
                is_pleasant=True,
                reward="Никакого вознаграждения",
                linked_habit=self.pleasant_habit
            )
            habit.full_clean()

    def test_frequency_validation(self):
        """Проверка валидации периодичности"""
        with self.assertRaises(ValidationError):
            habit = Habit(
                user=self.user,
                action="Бег",
                frequency=0  # Ниже минимального значения
            )
            habit.full_clean()

    def test_duration_validation(self):
        """Проверка максимальной длительности"""
        with self.assertRaises(ValidationError):
            habit = Habit(
                user=self.user,
                action="Йога",
                duration=121  # Превышает максимальное значение
            )
            habit.full_clean()

    def test_habit_str_representation(self):
        """Проверка строкового представления"""
        habit = Habit.objects.create(
            user=self.user,
            action="Пить воду",
            time=datetime.time(10, 0)
        )
        self.assertIn("Пить воду", str(habit))
        self.assertIn("test@example.com", str(habit))
