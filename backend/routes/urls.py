"""
Маршрутизация для приложения routes.
"""

from django.urls import path

from .views import RouteCreateAPIView


urlpatterns = [
    path("", RouteCreateAPIView.as_view(), name="create_route"),
]