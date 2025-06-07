from rest_framework import serializers
from .models import Habit
from .validators import (
    validate_pleasant_habit,
    validate_reward_or_linked_habit,
    validate_duration
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user', 'created_at')

    def validate(self, data):
        # Проверка валидаторов
        validate_reward_or_linked_habit(data)
        if data.get('linked_habit'):
            validate_pleasant_habit(data['linked_habit'])
        if 'duration' in data:
            validate_duration(data['duration'])

        # Приятная привычка не может иметь вознаграждения
        if data.get('is_pleasant') and data.get('reward'):
            raise serializers.ValidationError(
                'Приятная привычка не может иметь вознаграждения!'
            )

        return data

