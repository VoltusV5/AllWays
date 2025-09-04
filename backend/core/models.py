from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

# Менеджер для кастомного пользователя
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if not password:
            raise ValueError("Superusers must have a password.")
        return self.create_user(email, password, **extra_fields)

# Кастомная модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255, blank=True)  # для совместимости с твоим полем
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # обязательно для админки
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    failed_attempts = models.IntegerField(default=0)
    email_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# Остальные модели с привязкой к кастомному пользователю через settings.AUTH_USER_MODEL
class SocialLogin(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_logins"
    )
    provider = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class LoginHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="login_history"
    )
    login_at = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255, blank=True)
    browser = models.CharField(max_length=255, blank=True)
    success = models.BooleanField(default=True)

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("info", "Info"),
        ("booking_update", "Booking update"),
        ("promo", "Promo"),
        ("reminder", "Reminder"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    related_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

class AccountLevel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bonus_percent = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile", primary_key=True
    )
    full_name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    preferences = models.JSONField(default=dict)
    account_level = models.ForeignKey(
        AccountLevel, on_delete=models.SET_NULL, null=True, blank=True
    )
