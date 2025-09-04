from django.db import models

class AuditLog(models.Model):
    # Вместо прямого импорта User используем строку "core.User"
    user = models.ForeignKey(
        "core.User",  # строковая ссылка на модель
        on_delete=models.SET_NULL,
        null=True,
        related_name="audit_logs"
    )
    action = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    device_info = models.CharField(max_length=255, blank=True)
