from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    failed_attempts = models.IntegerField(default=0)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class SocialLogin(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="social_logins")
    provider = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class LoginHistory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="login_history")
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
        User, on_delete=models.CASCADE, related_name="notifications")
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
        User, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    full_name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    preferences = models.JSONField(default=dict)
    account_level = models.ForeignKey(
        AccountLevel, on_delete=models.SET_NULL, null=True, blank=True)
