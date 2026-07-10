"""
URL configuration for allways_project.
"""

from django.contrib import admin
from django.urls import include, path, re_path

from core.views import FrontendAppView


urlpatterns = [
    # Админ-панель
    path("admin/", admin.site.urls),
    
    # API эндпоинты
    path("api/users/", include("users.urls")),
    path("api/routes/", include("routes.urls")),
    
    # SPA (Vue.js) маршрутизатор
    # Перехватывает все пути, кроме начинающихся с 'admin/' или 'api/',
    re_path(r"^(?!admin/|api/).*$", FrontendAppView.as_view(), name="home"),
]
