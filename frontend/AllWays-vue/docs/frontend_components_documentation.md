# 📘 Документация по Vue-компонентам проекта AllWays

## Общая структура проекта, компоненты
Проект разбит на независимые **Vue-компоненты**, некоторые из которых могут переиспользоваться на разных страницах.  

### Главные страницы
- **MainPage** – экран с картой и маршрутами (начальная страница)
- **AuthPage** – экран авторизации (вход, ввод пароля)  
- **RegisterPage** – экран регистрации  

---

## 🔹 Компоненты для экрана с картой (*MainPage*)

### AppHeader (Header ????)
- Логотип **AllWays**  
- Иконка профиля пользователя (аватар)  

### Map
Основной компонент карты.  
Включает в себя:
- Яндекс карту и все надстройки, которые мы будем добавлять в процессе разработки, например:
  - **RoutePath????** – отрисовка маршрутов (линии, шаги, транспорт)  
  - **RouteMarkers?????** – остановки, станции метро, иконки транспорта  
  - **MapControls** – кнопки управления картой (масштабирование, навигация)  


### BottomPanel?????
Панель внизу с поиском и фильтрами.  
Состав:
- **SearchBar** – поле поиска + иконки "лупа" и "закладки"  
- **TransportFilters** – кнопки фильтров: *все, автобус, метро, трамвай, поезд, самолёт и т.д.*  
- **Slider** - ...

---

## 🔹 Компоненты для авторизации и регистрации (*AuthPage, RegisterPage*) ???????????

### AuthForm
- Блок для ввода **email / логина**  
- Кнопка **"Войти"**  
- Кнопка **"Создать аккаунт"**  

### PasswordForm
- Ввод пароля для конкретного аккаунта  
- Кнопка **"Войти"**  
- Ссылка **"Не помню пароль"**  

### RegisterForm
Поля:
- Логин  
- Почта  
- Пароль  
- Повтор пароля  
- Чекбокс *"Принимаю политику конфиденциальности"*  

Кнопки:
- **"Создать аккаунт"**  
- **"Уже есть аккаунт"**  

### SocialLogin
Кнопки авторизации через сторонние сервисы:  
*Яндекс, ВКонтакте, Mail, Одноклассники, Google*  

### AuthHeader
- Логотип **AllWays**  
- Текстовый слоган: *"Создайте аккаунт, чтобы покупать билеты и сохранять поездки"*  
- Кнопка **"назад"** (стрелка)  



---
## 🚀 Пример роутера (router/index.js)
```js
import { createRouter, createWebHistory } from "vue-router";
import MapPage from "@/pages/MapPage.vue";
import AuthPage from "@/pages/AuthPage.vue";
import PasswordPage from "@/pages/PasswordPage.vue";
import RegisterPage from "@/pages/RegisterPage.vue";

const routes = [
  { path: "/", redirect: "/map" },
  { path: "/map", component: MapPage },
  { path: "/auth", component: AuthPage },
  { path: "/auth/password", component: PasswordPage },
  { path: "/register", component: RegisterPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```




