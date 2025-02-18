import { createRouter, createWebHashHistory } from "vue-router";
import LoginForm from "./components/LoginForm.vue";
import MainPage from "./components/MainPage.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [

        {path: '/login', component: LoginForm},
        {path: '/home', component: MainPage},
    ]
})