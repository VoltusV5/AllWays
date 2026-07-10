from django.core.validators import MinValueValidator
from django.db import models


class Segment(models.Model):
    """
    Модель отдельного сегмента внутри пользовательского маршрута.
    """
    user_route = models.ForeignKey(
        "UserRoute",
        on_delete=models.CASCADE,
        related_name="segments",
        verbose_name="route"
    )
    
    segment_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="segment number"
    )
    name = models.CharField(max_length=255, verbose_name="segment name")
    
    # Координаты (широта и долгота)
    start_point_lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="start latitude"
    )
    start_point_lon = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="start longitude"
    )
    end_point_lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="end latitude"
    )
    end_point_lon = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="end longitude"
    )
    
    duration = models.PositiveIntegerField(
        verbose_name="duration",
        help_text="Duration in minutes or seconds"
    )
    distance_km = models.PositiveIntegerField(
        verbose_name="distance (km)"
    )
    transport_type = models.CharField(
        max_length=50, 
        verbose_name="transport type",
        help_text="e.g. Train, Flight, Bus"
    )
    price = models.PositiveIntegerField(verbose_name="price")

    def __str__(self) -> str:
        return f"Segment {self.segment_number} of {self.user_route.name}"

    class Meta:
        verbose_name = "segment"
        verbose_name_plural = "segments"

        constraints = [
            models.UniqueConstraint(
                fields=["user_route", "segment_number"],
                name="unique_route_segment_number"
            )
        ]
        
        # Индекс для ускорения запросов вида "получить все сегменты маршрута X"
        indexes = [
            models.Index(fields=["user_route", "segment_number"]),
        ]