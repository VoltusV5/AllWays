from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Проверка паролей
        if password1 != password2:
            return render(request, "users/register.html", {"error": "Пароли не совпадают."})

        # Проверка, есть ли уже такой email
        if User.objects.filter(email=email).exists():
            return render(request, "users/register.html", {"error": "Email уже используется."})

        # Создаём пользователя
        user = User.objects.create_user(email=email, password=password1)
        return redirect("login")  # Перенаправляем на страницу логина

    return render(request, "users/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # Главная или профиль
        else:
            return render(request, "users/login.html", {"error": "Неверный email или пароль."})

    return render(request, "users/login.html")
