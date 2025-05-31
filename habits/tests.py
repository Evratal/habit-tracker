import pytest
from django.core.exceptions import ValidationError
from habits.models import Habit
from users.models import User

@pytest.mark.django_db
def test_habit_creation():
    user = User.objects.create(email='test@example.com')
    habit = Habit.objects.create(
        user=user,
        place='Дом',
        time='09:00:00',
        action='Пить воду',
        duration=30,
        frequency=1
    )
    assert habit.action == 'Пить воду'
    assert habit.user.email == 'test@example.com'

@pytest.mark.django_db
def test_habit_duration_validation():
    user = User.objects.create(email='test@example.com')
    habit = Habit(
        user=user,
        place='Дом',
        time='09:00:00',
        action='Пить воду',
        duration=150,  # > 120 секунд
        frequency=1
    )
    with pytest.raises(ValidationError):
        habit.full_clean()