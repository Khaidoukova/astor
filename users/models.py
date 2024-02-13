from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    office_number = models.IntegerField(verbose_name='номер помещения', null=True, blank=True)
    company = models.CharField(max_length=50, verbose_name='компания', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='имя', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='телефон', null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_manager = models.BooleanField(default=False, verbose_name='Менеджер')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
