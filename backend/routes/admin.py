"""
Настройки админ-панели для приложения routes.
"""

from django.contrib import admin

from .models import Segment, UserRoute


class SegmentInline(admin.TabularInline):
    """
    Позволяет редактировать сегменты прямо внутри страницы маршрута.
    """
    model = Segment
    # Не показывать пустые формы по умолчанию
    extra = 0 
    ordering = ["segment_number"]


@admin.register(UserRoute)
class UserRouteAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "general_start_point", "general_end_point", "created_at"]
    search_fields = ["name", "user__email"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at", "updated_at"]
    
    inlines = [SegmentInline]


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ["segment_number", "name", "user_route", "transport_type", "price"]
    search_fields = ["name", "user_route__name"]
    list_filter = ["transport_type"]
