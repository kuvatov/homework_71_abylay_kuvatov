from django.contrib.auth import get_user_model
from django.db import models


class Like(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    publication = models.ForeignKey(
        to='instagram.Publication',
        on_delete=models.CASCADE,
        verbose_name='Публикация',
        related_name='likes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
