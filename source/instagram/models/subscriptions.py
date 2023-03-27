from django.contrib.auth import get_user_model
from django.db import models


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
