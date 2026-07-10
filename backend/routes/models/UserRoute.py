"""
Модель пользовательского маршрута.
"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class UserRoute(models.Model):
    """
    Главная сущность маршрута, который составляет пользователь.
    Включает в себя общие начальную и конечную точки, а также содержит вложенные сегменты.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="routes",
        verbose_name="user"
    )
    name = models.CharField(max_length=255, verbose_name="route name")
    general_start_point = models.CharField(max_length=255, verbose_name="general start point")
    general_end_point = models.CharField(max_length=255, verbose_name="general end point")

    created_at = models.DateTimeField(default=timezone.now, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        verbose_name = "user route"
        verbose_name_plural = "user routes"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} ({getattr(self.user, 'email', self.user_id)})"
