import { createRouter, createWebHistory } from "vue-router"
import MainPage from "@/views/MainPage.vue"

const routes = [
    { path: "/", name: "Home", component: MainPage }
]

export default createRouter({
    history: createWebHistory(),
    routes
})
