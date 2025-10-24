from django.contrib import admin
from core.models import User
from routes.models import UserRoute, Segment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'email_verified')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )




