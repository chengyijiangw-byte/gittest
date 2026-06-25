import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index.js";

const app = createApp(App)
// createApp(App).mount('#app')
app.use(router) //使用路由功能
app.mount('#app')