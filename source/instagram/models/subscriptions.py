from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        to=get_user_model(),
        related_name='subscriptions',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    subscribed_to = models.ForeignKey(
        to=get_user_model(),
        related_name='subscribers',
        on_delete=models.CASCADE,
        verbose_name='Подписка'
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

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
