import './assets/styles.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'   // <-- импортируем роутер

const app = createApp(App)

app.use(router)                 // <-- подключаем роутер
app.mount('#app')
