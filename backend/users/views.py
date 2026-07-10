"""
Views для приложения users.
"""

from django.contrib.auth import authenticate, get_user_model, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegisterSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    """
    Регистрация нового пользователя.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Пользователь успешно зарегистрирован"}, 
                status=status.HTTP_201_CREATED
            )
            
        errors = serializer.errors
        first_error_msg = list(errors.values())[0][0] if errors else "Ошибка валидации"
        if "error" in errors:
            first_error_msg = errors["error"][0]
            
        return Response({"error": first_error_msg}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    Авторизация пользователя (Session Auth).
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": "Email и пароль обязательны"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.validated_data["email"].lower()
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Успешная авторизация"}, status=status.HTTP_200_OK)
            
        return Response({"error": "Неверный email или пароль"}, status=status.HTTP_400_BAD_REQUEST)


class CheckEmailAPIView(APIView):
    """
    Проверка занят/свободен email.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email обязателен"}, status=status.HTTP_400_BAD_REQUEST)
            
        email = email.lower()
        exists = User.objects.filter(email__iexact=email).exists()
        
        return Response({"exists": exists}, status=status.HTTP_200_OK)
