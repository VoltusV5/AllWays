from pathlib import Path
import os
from dotenv import load_dotenv

# Подгружаем переменные из .env
load_dotenv()

# Указываем корень проекта (AllWays/backend)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ON_SERVER = 0
DEBUG = True


# Конфигурация базы данных
if ON_SERVER == "1":
    # Если ON_SERVER=1 (продакшн), используем MySQL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("MYSQL_DB_NAME", "VoltusV$default"),
            "USER": os.getenv("MYSQL_USER", "VoltusV"),
            "PASSWORD": os.getenv("MYSQL_PASSWORD", "c~yRP6#XnE4M"),
            "HOST": os.getenv("MYSQL_HOST", "VoltusV.mysql.pythonanywhere-services.com"),
            "PORT": os.getenv("MYSQL_PORT", "3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
            },
        }
    }
else:
    # Если ON_SERVER=0 (локальное окружение), используем SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # Файл базы данных для локальной разработки
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

AUTH_USER_MODEL = 'core.User'

# Установленные приложения
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "users",
    'routes',
    'rest_framework',
]


CSRF_COOKIE_NAME = 'csrftoken'  # Имя cookie для CSRF токена
CSRF_TRUSTED_ORIGINS = [
    'https://yourdomain.com',   # Ваш домен
    'http://localhost:8080',    # Для локальной разработки
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Стандартный бэкенд
]

# Настройки статических файлов
STATIC_URL = "/static/"

if ON_SERVER:
    # Настройки для сервера (например, использование `collectstatic`)
    STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic собирает сюда
    STATICFILES_DIRS = [
        BASE_DIR / "backend" / "static",  # свои css/js
        BASE_DIR / "backend" / "frontend" / "dist" / "assets",  # Vue ассеты
    ]
    VUE_DIST_DIR = BASE_DIR / "backend" / "frontend" / "dist"
else:
    # Настройки для локальной разработки (без использования `collectstatic`)
    STATICFILES_DIRS = [
        BASE_DIR / "frontend" / "dist",  # Папка, где лежат скомпилированные файлы фронтенда
    ]
    STATIC_ROOT = BASE_DIR / "staticfiles"

VUE_DIST_DIR = BASE_DIR / "backend" / "frontend" / "dist"

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
