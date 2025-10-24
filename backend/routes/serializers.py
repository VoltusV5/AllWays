# routes/serializers.py
from rest_framework import serializers
from .models import UserRoute

class UserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoute
        fields = ['id', 'user', 'name', 'general_start_point', 'general_end_point']
        read_only_fields = ['id', 'user', 'name']  # Пользователь и имя задаются автоматически