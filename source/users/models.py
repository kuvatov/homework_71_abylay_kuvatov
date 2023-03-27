from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager


class SexChoice(TextChoices):
    MALE = 'male', 'Мужчина'
    FEMALE = 'female', 'Женщина'
    OTHER = 'other', 'Другое'


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        blank=True
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='Аватар'
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Имя'
    )
    user_information = models.TextField(
        blank=True,
        null=True,
        verbose_name='Информация о пользователе'
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )
    sex = models.CharField(
        max_length=10,
        choices=SexChoice.choices,
        blank=True,
        null=True,
        verbose_name='Пол'
    )
    publications_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик публикаций'
    )
    subscribers_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик подписчиков'
    )
    subscriptions_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик подписок'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время редактирования"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удален",
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()
