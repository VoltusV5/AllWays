"""
Сериализаторы для приложения users.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    Инкапсулирует в себе все проверки.
    """
    confirmPassword = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password", "confirmPassword"]

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email уже используется")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmPassword"]:
            raise serializers.ValidationError({"error": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirmPassword")
        
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user


class LoginSerializer(serializers.Serializer):
    """
    Сериализатор для валидации входных данных при логине.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
