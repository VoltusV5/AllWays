"""
Модели приложения core.
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    Кастомный менеджер пользователей.
    """

    def create_user(self, email: str, password: str = None, **extra_fields):
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

    def create_superuser(self, email: str, password: str = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if not password:
            raise ValueError("Superusers must have a password.")
            
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя с аутентификацией по email вместо username.
    """
    email = models.EmailField(unique=True, verbose_name="email address")
    
    is_active = models.BooleanField(default=True, verbose_name="active")
    is_staff = models.BooleanField(default=False, verbose_name="staff status")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")
    
    failed_attempts = models.IntegerField(default=0, verbose_name="failed login attempts")
    email_verified = models.BooleanField(default=False, verbose_name="email verified")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return self.email

