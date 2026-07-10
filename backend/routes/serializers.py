"""
Сериализаторы для приложения routes.
"""

from rest_framework import serializers

from .models import UserRoute


class UserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoute
        fields = [
            "id", 
            "user", 
            "name", 
            "general_start_point", 
            "general_end_point", 
            "created_at", 
            "updated_at"
        ]
        read_only_fields = ["id", "user", "name", "created_at", "updated_at"]