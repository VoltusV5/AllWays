# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/routes/', views.find_routes, name='find_routes'),
]
