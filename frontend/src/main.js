import './assets/styles.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'   // <-- импортируем роутер

const app = createApp(App)

// Глобальный обработчик ошибок
app.config.errorHandler = (err, instance, info) => {
    console.error('Global error handler:', err, info);
    // Можно добавить отправку ошибок в сервис мониторинга
}

app.use(router)                 // <-- подключаем роутер
app.mount('#app')