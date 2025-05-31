from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'habits/public/',
        HabitViewSet.as_view({'get': 'list'}),
        {'action': 'public'},
        name='public-habits'
    ),
]