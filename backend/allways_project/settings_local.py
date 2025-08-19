# settings_local.py
from pathlib import Path


# Включаем режим отладки
DEBUG = True

# Хосты для локального теста
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Путь к корню проекта, где лежит manage.py
BASE_DIR = Path(__file__).resolve().parent.parent  # поднимаемся на один уровень вверх из allways_project/

# Локальная база данных (SQLite для простоты)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Любые секреты для локального запуска
SECRET_KEY = 'django-insecure-замени-на-свой-ключ'
