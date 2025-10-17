
from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer

User = get_user_model()

# Регистрация пользователя
@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        confirmPassword = request.data.get("confirmPassword")
        
        if password != confirmPassword:
            return Response({"error": "Пароли не совпадают"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email уже используется"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, password=password)
        return Response({"message": "Пользователь успешно зарегистрирован"}, status=status.HTTP_201_CREATED)

# Авторизация пользователя
@api_view(['POST'])
def login_view(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response({"message": "Успешная авторизация"}, status=status.HTTP_200_OK)
        return Response({"error": "Неверный email или пароль"}, status=status.HTTP_400_BAD_REQUEST)

# Проверка существования email
@api_view(['POST'])
def check_email(request):
    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        return JsonResponse({'exists': True})
    return JsonResponse({'exists': False})
