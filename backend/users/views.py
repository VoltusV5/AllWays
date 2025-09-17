from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            return render(request, "users/register.html", {"error": "Email занят"})
        user = User.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect("/")  # или /profile
    return render(request, "users/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("/")  # или /profile
        return render(request, "users/login.html", {"error": "Неверный email или пароль"})
    return render(request, "users/login.html")
