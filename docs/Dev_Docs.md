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

### 2. Организация папок и файлов

```bash

backend/	  Сервер на Django, приложения, виртуальное окружение Python
frontend/	    Vue.js SPA — исходники фронтенда и конфигурация npm
mobile/	     Android-проект на Java с WebView
docs/	      Общая документация проекта
scripts/	    Скрипты для миграций, деплоя и других задач

```


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

### 2. Структура репозитория
####  есть в отдельной документации направления в backend/docs frontend/docs и т.п.


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
Структура папок frontend находится в frontend/docs/Project structure.md



---

### 3.3. Мобильное приложение (Android WebView на Java)



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
# Все изменения должны проходить через Pull Request

# После того, как вы выполнили задачу - присылаете её командиру. Он говорит, что всё ок, и только после этого ветка с изменениями сливается в develop

# Нельзя пушить напрямую в main или develop — только через PR.

```


---

### 6. Полезные советы

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
<br><br><br><br><br>

# Приложение:

---

### CI/CD
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