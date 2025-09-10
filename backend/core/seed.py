# core/seed.py
from core.models import User, Profile, Notification, AccountLevel, LoginHistory
from django.utils import timezone

def run():
    # Уровни аккаунтов
    free, _ = AccountLevel.objects.get_or_create(name="Free", defaults={"description": "Бесплатный уровень"})
    premium, _ = AccountLevel.objects.get_or_create(name="Premium", defaults={"description": "Платный тариф"})

    # Пользователи
    user1, _ = User.objects.get_or_create(email="user1@example.com")
    user1.set_password("12345")
    user1.save()
    
    user2, _ = User.objects.get_or_create(email="user2@example.com")
    user2.set_password("12345")
    user2.save()

    # Профили
    Profile.objects.get_or_create(user=user1, defaults={"full_name": "First User", "account_level": free})
    Profile.objects.get_or_create(user=user2, defaults={"full_name": "Second User", "account_level": premium})

    # Уведомления
    Notification.objects.get_or_create(user=user1, message="Ваше бронирование подтверждено", defaults={"type": "info"})
    Notification.objects.get_or_create(user=user2, message="Оплата ещё не поступила", defaults={"type": "info"})

    # Лог входа
    LoginHistory.objects.get_or_create(user=user1, login_at=timezone.now(), defaults={"ip": "127.0.0.1"})
    LoginHistory.objects.get_or_create(user=user2, login_at=timezone.now(), defaults={"ip": "127.0.0.2"})

    print("База заполнена")
