"""
Маршрутизация для приложения users.
"""

from django.urls import path

from .views import CheckEmailAPIView, LoginAPIView, RegisterAPIView


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("check-email/", CheckEmailAPIView.as_view(), name="check_email"),
]
