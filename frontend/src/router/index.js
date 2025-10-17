import { createRouter, createWebHistory } from "vue-router"
import MainPage from "@/views/MainPage.vue"
import AuthorizationPageEmail from '@/views/AuthorizationPageEmail.vue'
import AuthorizationPagePassword from '@/views/AuthorizationPagePassword.vue'
import RegistrationPage from '@/views/RegistrationPage.vue'
import RouteBuilder from "@/views/RouteBuilder.vue"

const routes = [
    { path: "/", name: "Home", component: MainPage },
    { path: '/authorization-email', name: 'AuthorizationPageEmail', component: AuthorizationPageEmail },
    { path: '/authorization-password', name: 'AuthorizationPagePassword', component: AuthorizationPagePassword },
    { path: '/registration', name: 'RegistrationPage', component: RegistrationPage },
    { path: '/build-route', name: 'RouteBuilder', component: RouteBuilder },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router