from django.core.exceptions import ValidationError

def validate_pleasant_habit(value):
    """Проверка, что связанная привычка является приятной."""
    if value and not value.is_pleasant:
        raise ValidationError(
            'Связанная привычка должна быть приятной!'
        )

def validate_reward_or_linked_habit(data):
    """Запрет одновременного указания вознаграждения и связанной привычки."""
    if data.get('reward') and data.get('linked_habit'):
        raise ValidationError(
            'Укажите только вознаграждение ИЛИ связанную привычку!'
        )

def validate_duration(value):
    """Проверка времени выполнения (макс. 120 секунд)."""
    if value > 120:
        raise ValidationError(
            'Время выполнения не может превышать 120 секунд!'
        )