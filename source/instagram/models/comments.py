from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    publication = models.ForeignKey(
        to='instagram.Publication',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация'
    )
    text = models.TextField(
        max_length=2000,
        verbose_name='Текст'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время редактирования"
    )
