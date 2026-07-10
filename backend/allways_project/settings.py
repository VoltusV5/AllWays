"""
Django settings for allways_project.
"""

from pathlib import Path

import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    IS_PRODUCTION=(bool, False),
)

env_file = BASE_DIR / '.env'
if env_file.exists():
    environ.Env.read_env(env_file)


# ==========================================
# 1. ОСНОВНЫЕ НАСТРОЙКИ
# ==========================================

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')
IS_PRODUCTION = env('IS_PRODUCTION')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

ROOT_URLCONF = "allways_project.urls"
WSGI_APPLICATION = "allways_project.wsgi.application"
AUTH_USER_MODEL = 'core.User'


# ==========================================
# 2. БАЗА ДАННЫХ
# ==========================================
if IS_PRODUCTION:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("MYSQL_DB_NAME"),
            "USER": env("MYSQL_USER"),
            "PASSWORD": env("MYSQL_PASSWORD"),
            "HOST": env("MYSQL_HOST"),
            "PORT": env("MYSQL_PORT", default="3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ==========================================
# 3. ПРИЛОЖЕНИЯ И MIDDLEWARE
# ==========================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "core",
    "users",
    "routes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# ==========================================
# 4. СТАТИКА И ШАБЛОНЫ
# ==========================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

if IS_PRODUCTION:
    STATICFILES_DIRS = [
        BASE_DIR / "backend" / "static",
        BASE_DIR / "backend" / "frontend" / "dist" / "assets",
    ]
else:
    STATICFILES_DIRS = [
        BASE_DIR / "frontend" / "dist",
    ]

VUE_DIST_DIR = BASE_DIR / "backend" / "frontend" / "dist"

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


# ==========================================
# 5. БЕЗОПАСНОСТЬ
# ==========================================
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS',
    default=['http://localhost:8080', 'http://127.0.0.1:8080']
)


# ==========================================
# 6. ЛОГИРОВАНИЕ
# ==========================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "backend" / "django.log",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console", "file"] if IS_PRODUCTION else ["console"],
        "level": env("LOG_LEVEL", default="INFO"),
    },
}
