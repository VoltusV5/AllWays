from pathlib import Path
import os
from dotenv import load_dotenv

# Подгружаем переменные из .env
load_dotenv()

# Указываем корень проекта (AllWays/backend)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Настройки базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Секретный ключ
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-замени-на-ключ")

# DEBUG включается только если в .env указано True
DEBUG = os.getenv("DEBUG", "True") == "True"

# Разрешённые хосты
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'voltusv.pythonanywhere.com'
]

# Установленные приложения
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Настройки статических файлов
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic собирает сюда
STATICFILES_DIRS = [
    BASE_DIR / "backend" /  "static",  # если есть свои css/js
]

# Простейшая конфигурация middleware (нужна для работы админки)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# Корень URL
ROOT_URLCONF = "allways_project.urls"

# Шаблоны (можно минимально)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = "allways_project.wsgi.application"

