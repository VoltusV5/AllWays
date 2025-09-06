# 📖 Документация по фронтенд-разработке (Vue.js проект)

## 🚀 Общая структура проекта

```bash
src/
├── assets/                # картинки, иконки, шрифты, общие (глобальные) стили css, лого
│   ├── styles.css
│   ├── images/
│
├── components/            # переиспользуемые компоненты
│   ├── layout/            # общие блоки интерфейса (повторяющиеся на разных страницах компоненты, такие как заголовок, футер и тд)
│   │   ├── AppHeader.vue
│   │   ├── BottomPanel.vue #????? - возможно, будет исправлено/изменено название/полностью файл/удален
│   │   └── FloatingButtons.vue #?????
│   │
│   ├── Main_page/ # главная страница сайта
│   │   ├── Header.vue # загаловок (возможно - AppHeader.vue - глобальный)
│   │   ├── Map.vue # встроенная Яндекс карта
│   │   ├── MapControls.vue # кнопки управления картой ????????
│   │   ├── SearchBar.vue # поисковик ... 
│   │   ├── Slider.vue # для ...
│   │   └── TransportFilters.vue # панель фильтров видов транспорта
│   │

│   ├── Route/         # настройка маршрута     
│   │   ├── 
│   │   ├── RoutePath.vue #????? - возможно, будет исправлено/изменено название/полностью файл/удален
│   │   ├── RouteMarkers.vue #?????
│   │   └── MapControls1.vue #?????
│   │
│   ├── Registration/              # авторизация/регистрация
│   │   ├── AuthHeader.vue #?????
│   │   ├── AuthForm.vue #?????
│   │   ├── PasswordForm.vue #?????
│   │   ├── RegisterForm.vue #?????
│   │   └── SocialLogin.vue #?????
│   │
│   ├── ui/                # универсальные UI-элементы (повторяющеюся элементы, такие как кнопки, поля ввода и тд)
│   │   ├── InputField.vue #?????
│   │   ├── PrimaryButton.vue #?????
│   │   ├── Checkbox.vue #?????
│   │   ├── IconButton.vue #?????
│   │   └── FilterButton.vue #?????
│   │
│   └── shared/   #?????         # вспомогательные маленькие компоненты
│       └── RouteInfoPopup.vue #?????
│
├── views/                 # страницы (роуты)
│   ├── MainPage.vue
│   ├── AuthPage.vue #?????
│   ├── PasswordPage.vue #?????
│   └── RegisterPage.vue #?????
│
├── store/   #?????              # Pinia-хранилище
│   ├── user.js      #?????      # авторизация, данные пользователя
│   ├── map.js       #?????      # маршруты, фильтры
│   └── settings.js  #?????      # UI-настройки
│
├── router/                # роутинг
│   └── index.js           # все пути (map, auth, register)
│
├── App.vue                # корневой компонент
└── main.js                # точка входа



```

