# allways_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import FrontendAppView  # импорт вашего класса
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # админка
    # ... любые другие backend-роуты

    # Всё остальное отдаём Vue
    re_path(r'^(?!admin/).*$', FrontendAppView.as_view(), name='home'),
]
