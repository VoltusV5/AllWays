# allways_project/urls.py
from django.contrib import admin
from django.urls import path, re_path
from core.views import FrontendAppView  # импорт вашего класса
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # админка
    # любой другой API- или backend-URL можно здесь добавить, например:
    # path('api/users/', include('users.urls')),

    # все остальные пути перенаправляем на Vue
    re_path(r'^.*$', FrontendAppView.as_view(), name='home'),
]
