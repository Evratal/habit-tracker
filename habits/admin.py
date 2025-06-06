from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'time', 'is_pleasant', 'is_public')
    list_filter = ('is_pleasant', 'is_public')
    search_fields = ('action', 'place', 'user__email')