# routes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_route, name='create_route'),
]