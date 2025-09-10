from django.contrib import admin
from django.urls import path, re_path
from core.views import FrontendAppView
from users.views import users_stub  # пример API-заглушки

urlpatterns = [
    # админка
    path('admin/', admin.site.urls),

    # API-заглушки (их можешь добавлять здесь или через include)
    path('api/users/', users_stub, name="users_stub"),

    # все остальные пути → Vue SPA
    re_path(r'^.*$', FrontendAppView.as_view(), name="frontend"),
]
