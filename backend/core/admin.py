"""
Настройки админ-панели для приложения core.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """
    Настройки отображения кастомной модели User в админ-панели.
    """
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'email_verified', 'created_at')
    search_fields = ('email',)
    
    readonly_fields = ('last_login', 'created_at')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
