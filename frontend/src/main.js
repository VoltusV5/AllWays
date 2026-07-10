import './assets/styles.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.withCredentials = true;

const app = createApp(App)

app.config.errorHandler = (err, instance, info) => {
    console.error('Global error handler:', err, info);
}

app.use(router)
app.mount('#app')