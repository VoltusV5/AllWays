import os
from pathlib import Path
from dotenv import load_dotenv

# Подгружаем переменные из .env
load_dotenv()

# Указываем корень проекта (AllWays/backend)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Настройки базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "VoltusV$default",
        "USER": "VoltusV",
        "PASSWORD": "c~yRP6#XnE4M",
        "HOST": "VoltusV.mysql.pythonanywhere-services.com",
        "PORT": "3306",
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}

# Секретный ключ
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-замени-на-ключ")

# === НАСТРОЙКИ Яндекс.Расписания ===
YANDEX_SCHEDULE_API_KEY = os.getenv("YANDEX_SCHEDULE_API_KEY")
YANDEX_SCHEDULE_BASE_URL = os.getenv(
    "YANDEX_SCHEDULE_BASE_URL", "https://api.rasp.yandex.net/v3.0")
YANDEX_REQUEST_TIMEOUT = int(os.getenv("YANDEX_REQUEST_TIMEOUT", "30"))
YANDEX_MAX_RETRIES = int(os.getenv("YANDEX_MAX_RETRIES", "3"))

YANDEX_SCHEDULE_CONFIG = {
    'API_KEY': YANDEX_SCHEDULE_API_KEY,
    'BASE_URL': YANDEX_SCHEDULE_BASE_URL,
    'TIMEOUT': YANDEX_REQUEST_TIMEOUT,
    'MAX_RETRIES': YANDEX_MAX_RETRIES,
    'TRANSPORT_TYPES': 'train,plane,suburban,bus',  # можно вынести в .env
}

# DEBUG включается только если в .env указано True
DEBUG = os.getenv("DEBUG", "True") == "True"

# Разрешённые хосты
allowed_hosts_env = os.getenv("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'voltusv.pythonanywhere.com'
] + ([host.strip() for host in allowed_hosts_env.split(',')] if allowed_hosts_env else [])

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
]


# Настройки статических файлов
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic собирает сюда

# Пути, откуда брать статику
STATICFILES_DIRS = [
    BASE_DIR / "backend" / "static",      # свои css/js
    BASE_DIR / "backend" / "frontend" / "dist" / "assets",  # Vue ассеты
]

# Логирование для отладки API запросов
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'yandex_schedule': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    },
}

# Путь к Vue build
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
