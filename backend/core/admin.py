from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, AccountLevel, Notification, SocialLogin, LoginHistory

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "email_verified")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Profile)
admin.site.register(AccountLevel)
admin.site.register(Notification)
admin.site.register(SocialLogin)
admin.site.register(LoginHistory)
