# 📚 Руководство по работе с проектом AllWays

## 1. Введение
**AllWays** — мультиплатформенный сервис для построения комбинированных маршрутов и оплаты билетов.  
В проекте участвуют:
- **Backend** — Django (Python)
- **Frontend** — Vue.js
- **Мобильное приложение** — Android WebView (Java)
- **Инфраструктура** — CI/CD

**Цель инструкции** — помочь новичку быстро настроить окружение и понять рабочий процесс в команде.

---


### 2. Структура репозитория
<pre>
.gitattributes           ← правила для Git: нормализация перевода строк, пометки бинарных файлов, Git LFS
.gitignore               ← список файлов/папок, которые не должны попадать в репозиторий (venv, __pycache__, .env и т.д.)
LICENSE                  ← лицензия проекта: юридические условия использования кода
README.md                ← Описание проекта

.github/                 ← настройки GitHub (CI/CD, issue templates и т.п.)
└── workflows/           ← пайплайны GitHub Actions
    └── deploy.yml       ← сценарий деплоя: сборка, тестирование, выкладка на сервер/облако

backend/                 ← папка с бэкендом (Django)
├── manage.py            ← точка входа для Django CLI (runserver, migrate, createsuperuser, test и т.п.)
├── requirements.txt     ← список зависимостей Python для бэкенда
├── README.md            ← инструкция именно для backend: локальный запуск, миграции, Celery и т.п.
├── allways_project/     ← конфигурация Django-проекта (ядро)
│   ├── __init__.py      ← помечает папку как Python-пакет
│   ├── asgi.py          ← точка входа для async-серверов (Uvicorn/Daphne, WebSockets)
│   ├── settings.py      ← глобальные настройки Django: базы, кэш, приложения, middleware
│   ├── urls.py          ← корневые маршруты проекта (подключение admin, API, app-urls)
│   └── wsgi.py          ← точка входа для WSGI-серверов (Gunicorn/uWSGI, классический деплой)
├── notifications/       ← приложение для уведомлений (email/SMS/push)
│   ├── models.py        ← модели уведомлений, подписок, статусов
│   ├── serializers.py   ← сериализация уведомлений в API (DRF)
│   ├── tasks.py         ← фоновые задачи (Celery): отправка уведомлений
│   ├── tests.py         ← тесты уведомлений
│   ├── urls.py          ← маршруты API уведомлений
│   └── views.py         ← контроллеры/эндпоинты API уведомлений
├── payments/            ← приложение для платежей
│   ├── models.py        ← модели транзакций, счетов, статусов
│   ├── serializers.py   ← сериализация платежных данных
│   ├── tasks.py         ← фоновые задачи (обработка webhooks, подтверждение платежей)
│   ├── tests.py         ← тесты платежей
│   ├── urls.py          ← маршруты API платежей
│   └── views.py         ← контроллеры/эндпоинты платежей
├── routing/             ← приложение для маршрутов/поиска
│   ├── models.py        ← модели маршрутов, сегментов, расписаний
│   ├── serializers.py   ← сериализация маршрутов
│   ├── tasks.py         ← фоновые задачи (обновление расписаний, кеширование)
│   ├── tests.py         ← тесты поиска маршрутов
│   ├── urls.py          ← маршруты API маршрутов
│   └── views.py         ← контроллеры/эндпоинты поиска маршрутов
└── users/               ← приложение для пользователей
    ├── models.py        ← модели пользователей, профилей, ролей
    ├── serializers.py   ← сериализация данных пользователей
    ├── tasks.py         ← фоновые задачи (активация, уведомления)
    ├── tests.py         ← тесты пользователей и авторизации
    ├── urls.py          ← маршруты API пользователей
    └── views.py         ← контроллеры/эндпоинты (регистрация, логин, профиль)

frontend/                  ← папка фронтенда на Vue.js
├── .gitignore             ← локальные игнорируемые файлы (node_modules, build-артефакты)
├── README.md              ← инструкция по запуску/сборке фронта
├── jsconfig.json          ← конфиг для IDE: алиасы путей, автодополнение
├── package.json           ← список зависимостей, скриптов (npm run serve/build/test)
├── package-lock.json      ← фиксированные версии зависимостей (для воспроизводимости сборки)
├── public/                ← статические ресурсы, которые напрямую попадают в билд
│   ├── favicon.ico        ← иконка вкладки браузера
│   └── index.html         ← основной HTML-шаблон приложения
├── src/                   ← исходный код фронтенда
│   ├── App.vue            ← корневой Vue-компонент
│   ├── main.js            ← точка входа (инициализация Vue-приложения)
│   ├── assets/            ← папка для картинок/шрифтов/стилей
│   │   └── logo.png       ← пример ассета (логотип)
│   └── components/        ← переиспользуемые Vue-компоненты
│       └── HelloWorld.vue ← пример компонента
└── vue.config.js          ← конфигурация сборки (webpack/devServer/proxy и пр.)

mobile/               ← папка мобильного приложения
└── README.md         ← инструкция: где код мобильной части, как запускать (обычно Android/iOS)

scripts/                 ← вспомогательные скрипты для DevOps/разработки
├── README.md            ← описание, что делает каждый скрипт
├── deploy.sh            ← скрипт деплоя (сборка, копирование, рестарт сервисов)
├── migrate.sh           ← запуск Django миграций (обновление базы)
└── run_celery.sh        ← запуск Celery воркеров (фоновая обработка задач)

docs/                                 ← проектная документация
├── Dev_Docs.md                       ← основные dev-доки: как развернуть, архитектура
├── photo/                            ← скриншоты для документации
│   ├── about_tests.png               ← иллюстрация про тесты
│   └── env.png                       ← скрин окружения/переменных
├── shablon/                          ← шаблоны документации (guides, стандарты)
│   ├── api_specification.md          ← описание API
│   ├── architecture.md               ← архитектурное описание проекта
│   ├── coding_guidelines.md          ← правила кодинга (стиль, формат, lint)
│   ├── deployment_guide.md           ← как деплоить проект (шаги, окружение)
│   └── testing_guide.md              ← гайд по тестированию
├── Описание проекта.docx             ← Word-файл с описанием проекта
├── Описание технологий.docx          ← Word-файл с обзором технологий
└── Техническое задание.docx          ← Word-файл с формальным ТЗ


</pre>

---

## 3. Настройка окружения и запуск проекта

### 3.1. Backend (Python/Django)
```bash
# Перейти в папку backend
cd backend

# Создать виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
# Windows:
venv\Scripts\activate
# или
source venv/Scripts/activate
# Linux/macOS:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
# Или, если порт занят
python manage.py runserver 127.0.0.1:9000

# После этого сайт будет доступен в браузере по адресу:
http://127.0.0.1:8000/  # или 9000, если указал другой порт

```
Примечание:
``` bash
# python manage.py migrate
Применяет миграции — т.е. обновляет структуру базы данных на основе моделей Python (создаёт таблицы, добавляет поля и т.д.).
📌 Это нужно запускать каждый раз, когда меняется структура моделей (models.py).

# python manage.py runserver
Запускает локальный сервер разработки Django (по умолчанию на http://127.0.0.1:8000).
📌 Используется для тестов и отладки, в продакшене будет другой способ запуска.
```

---

### 3.2. Frontend (Vue.js)

```bash
# Установите Node.js (например, node-v22.18.0-x64.msi)
# Для загрузки наберите в браузере: 
node.js

# Перейти в папку frontend
cd ../frontend

# Установить зависимости npm
npm install

# Запустить dev-сервер
npm run serve

# Откройте браузер по адресу, который выведется в консоли (обычно http://localhost:8080)
```
Структура папок frontend
```bash
frontend/
│
├── public/         # Статические файлы (favicon, index.html)
├── src/            # Исходный код фронтенда
│   ├── assets/     # Картинки, стили, шрифты
│   ├── components/ # Мелкие переиспользуемые Vue-компоненты
│   ├── views/      # Страницы (маршруты)
│   ├── router/     # Настройка маршрутизации
│   ├── store/      # Vuex (хранилище состояния)
│   └── App.vue     # Корневой компонент
│
└── package.json    # Зависимости и скрипты

```
👉 Весь код пишется в frontend/src/ — компоненты, страницы, стили и т.д.
public/ используется в основном для статики и HTML-шаблона.


---

### 3.3. Мобильное приложение (Android WebView на Java)
``` bash
# 1. Откройте Android Studio.
# 2. Откройте папку проекта:
    /mobile/android_webview_app

# 3. Основная задача — создать WebView, который будет показывать веб-версию фронтенда (например, http://localhost:8080 или адрес продакшен-сервера).
```
```Java
// 4. Пример базового WebView в MainActivity.java:

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private WebView webView;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        webView = new WebView(this);
        setContentView(webView);

        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webView.loadUrl("http://your-frontend-url");
    }
}
```
```bash
# 5. Для полноценной разработки добавляйте новые активности, UI и связывайте с backend.
```

---


### 4. Работа с Git и ветвлением
``` bash
# 4.1. Основные ветки в репозитории
# main — стабильная ветка с продакшен-кодом.
# develop — ветка для интеграции новых функций.

# 4.2. Feature-ветки
# Для разработки новых функций используйте отдельные ветки по шаблону:

# Для мобильных:
feature/mobile/название_фичи
# Для фронтенда:
feature/frontend/название_фичи
# Для бэкенда:
feature/backend/название_фичи


# 4.3. Создание feature-ветки

git checkout develop
git pull origin develop
git checkout -b feature/frontend/login-form


# 4.4. Работа с feature-веткой

# Делайте коммиты локально.
# Пушьте ветку в удалённый репозиторий:
# git push -u origin feature/frontend/login-form
# Создавайте Pull Request (PR) в ветку develop через GitHub.

# 4.5 📝 Формат сообщений коммитов

feat: добавлен компонент авторизации
fix: исправлена ошибка отображения карты
docs: обновлено руководство
style: отформатирован код
refactor: упрощена логика маршрутов
test: добавлены тесты API


```

---

### 5. Pull Request и код-ревью

``` bash
# Все изменения должны проходить через Pull Request в ветку develop.

# Для слияния в develop требуется минимум 1-2 одобрения от коллег (обязательное код-ревью).

# Нельзя пушить напрямую в main или develop — только через PR.

# В PR обязательно проверяйте, что все тесты и линтеры проходят успешно.
```

---

### 6. CI/CD
# !!! Пока не настроено
``` bash
# 6.1. Что такое CI/CD?
CI (Continuous Integration) — автоматическая проверка кода (тесты, линтинг) при каждом PR и пуше.

# CD (Continuous Delivery/Deployment) — автоматический деплой приложения на сервер после успешных проверок.

# 6.2. В нашем проекте настроен GitHub Actions:
При пуше в develop или main запускаются тесты фронтенда и бэкенда.
Если тесты не проходят — PR не может быть замержен.


# По мере развития проекта можно добавить деплой в staging и production.

```

---

### 7. Организация папок и файлов

```bash

Папка	        Назначение
backend/	  Сервер на Django, приложения, виртуальное окружение Python
frontend/	    Vue.js SPA — исходники фронтенда и конфигурация npm
mobile/	     Android-проект на Java с WebView
docs/	  Документация проекта
scripts/	    Скрипты для миграций, деплоя и других задач

```

---

### 8. Полезные советы

```bash
# Перед началом работы всегда обновляй ветку develop:
git checkout develop
git pull origin develop

# Работай в своей feature-ветке — не трогай другие ветки.
# Часто коммить и пушь изменения, чтобы не потерять работу.

# Всегда создавай PR для внесения изменений.
# Уважай коллег, делай качественные ревью.
# Вопросы по проекту задавай в общем чате или напрямую.
```

---

# Важно, но пока не настроено.


![Настройка .env:](photo/env.png)

---

![Запуск тестов](photo/about_tests.png)

---

# CI/CD

```bash
5. CI/CD (GitHub Actions)
Для бэкенда (Django)
Создай .github/workflows/backend.yml:




name: Backend CI

on:
  pull_request:
    branches: [ develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: python manage.py test





Для фронтенда (Vue)
Создай .github/workflows/frontend.yml:


name: Frontend CI

on:
  pull_request:
    branches: [ develop ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: cd frontend && npm install && npm run build
```