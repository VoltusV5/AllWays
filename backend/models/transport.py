from django.db import models
from .users import User


class Provider(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, blank=True)


class Route(models.Model):
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="routes")
    name = models.CharField(max_length=255)


class Stop(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)


class Segment(models.Model):
    route = models.ForeignKey(
        Route, on_delete=models.CASCADE, related_name="segments")
    stop_from = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="segments_from")
    stop_to = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="segments_to")
    duration = models.IntegerField()
    distance_km = models.IntegerField()


class SegmentTransport(models.Model):
    segment = models.ForeignKey(
        Segment, on_delete=models.CASCADE, related_name="transports")
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="segment_transports")
    transport_type = models.CharField(max_length=100)
    price = models.IntegerField()
    distance_actual = models.IntegerField()
    duration_actual = models.IntegerField()
    segment_status = models.CharField(max_length=50)


class Schedule(models.Model):
    segment = models.ForeignKey(
        Segment, on_delete=models.CASCADE, related_name="schedules")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class UserRoute(models.Model):
    ROUTE_TYPES = (
        ("from_to", "From → To"),
        ("to_only", "To only"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="routes")
    route_type = models.CharField(max_length=20, choices=ROUTE_TYPES)
    start_stop = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="start_routes")
    end_stop = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="end_routes")
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    distance_km = models.IntegerField()
