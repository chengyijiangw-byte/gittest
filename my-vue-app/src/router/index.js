import {createRouter, createWebHistory} from 'vue-router'
//1.引入两个页面组件
import HomeView from "../views/HomeView.vue"
import DetailView from "../views/DetailView.vue"
import QuestionView from "../views/QuestionView.vue";
import TestSlotView from "../views/TestSlotView.vue";
//2.定义路由映射表
const routes = [
    {
        path: '/', //路由路径:当网页是主页时
        name: 'home',
        component: HomeView
    },
    {
        path: '/detail/:id', //路由路径:当网页是详情页时
        name: 'detail',
        component: DetailView
    },
    {
        path: '/exam',
        name: 'exam',
        component: QuestionView
    },
    {
        path: "/testslot",
        name: "testslot",
        component: TestSlotView
    }
]

//3.创建路由实例
const router = createRouter({
    history: createWebHistory(), // 使用Html5的历史记录模式
    routes // 路由映射表
})

export default router
