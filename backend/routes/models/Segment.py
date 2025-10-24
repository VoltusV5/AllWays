from django.db import models
from django.core.validators import MinValueValidator
from .UserRoute import UserRoute

class Segment(models.Model):
    user_route = models.ForeignKey(
        UserRoute,
        on_delete=models.CASCADE,
        related_name='segments'
    )
    segment_number = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=255)
    start_point_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    start_point_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    end_point_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    end_point_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    distance_km = models.IntegerField(validators=[MinValueValidator(0)])
    transport_type = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Segment {self.segment_number} of {self.user_route.name}"

    class Meta:
        verbose_name = "Segment"
        verbose_name_plural = "Segments"
        indexes = [
            models.Index(fields=['user_route', 'segment_number']),
        ]