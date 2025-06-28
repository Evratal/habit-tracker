from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Расширенная модель пользователя"""
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=20, blank=True, verbose_name='Telegram Chat ID')

    USERNAME_FIELD = 'email'  # Используем email для входа
    REQUIRED_FIELDS = ['username']  # Для createsuperuser

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email
