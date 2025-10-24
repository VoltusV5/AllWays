from django.db import models
from django.conf import settings

class UserRoute(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='routes'
    )
    name = models.CharField(max_length=255)
    general_start_point = models.CharField(max_length=255)
    general_end_point = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.user.email})"

    class Meta:
        verbose_name = "User Route"
        verbose_name_plural = "User Routes"