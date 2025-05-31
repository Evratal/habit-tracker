from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Только привычки текущего пользователя
        queryset = Habit.objects.filter(user=self.request.user)

        # Эндпоинт для публичных привычек
        if self.action == 'public':
            return Habit.objects.filter(is_public=True)

        return queryset

    def perform_create(self, serializer):
        # Автоматическое присвоение пользователя
        serializer.save(user=self.request.user)