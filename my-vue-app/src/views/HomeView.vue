<script setup>
import {ref, computed, watch} from 'vue'
import {useRouter} from "vue-router"; //1.引入useRouter工具
// 1. 引入点赞组件
import LikeWidget from '../components/LikeWidget.vue'
// 2.1引入留言板组件
import MessageBoard from '../components/MessageBoard.vue'

// 留言跳转详情
const router = useRouter() //2.创建一个路由实例
function goToDetail(index) {
  // 跳转到/detail/编号 这个网址
  router.push(`/detail/${index}`)
}

// 点赞板块
const likes = ref(0);
const visitorName = ref('神秘嘉宾')
// computed 会自动追踪 likes.value 的变化，并实时计算出最新的差值
// const remainingLikes = computed(() => 10 - likes.value)
// 2. 准备一个处理子组件信号的函数
function handleLikeEvent() {
  likes.value++ // 听到子组件喊“加点赞”时，我们就把自己的变量 +1
}

// 留言板块
// 尝试从本地存储 (localStorage) 中读取历史留言
const savedMessages = localStorage.getItem('my_vue_messages')
// 如果有保存的记录，就解析为数组；如果没有，就用默认的体验数据
const initialMessages = savedMessages ? JSON.parse(savedMessages) : ['vue真好玩', '我也来点个赞']
// 使用读取到的数据初始化响应式留言列表
const messages = ref(initialMessages)

// const messages = ref([
//   'Vue 真好玩',
//   '我也来点个赞',
//   '前端开发真有趣！'
// ])
// const newMessage = ref('')
//
// function submitMessage() {
//   if (newMessage.value.trim() !== '') {
//     messages.value.push(newMessage.value)
//     newMessage.value = ''
//   }
// }
// 2.2接收子组件传来的新留言内容 (content)，并保存到自己的大数组里
function handleAddMessage(content) {
  messages.value.push(content)
}

// 2.3 接收子组件传来的点击索引 (index)，并执行路由跳转
function handleGoToDetail(index) {
  router.push(`/detail/${index}`)
}

// 监控器：死死盯住 messages 数组的变化

watch(messages, (newMessages) => {
  // 一旦数组有变动（比如新增了留言），就立刻把最新列表存进本地存储
  localStorage.setItem('my_vue_messages', JSON.stringify(newMessages))
}, {deep: true}) // 开启深度监听，确保数组内部的变化也能被抓取到
</script>

<!--<template>-->
<!--  <div class="container">-->
<!--    <h1>欢迎，{{ visitorName }}的Vue应用</h1>-->
<!--    &lt;!&ndash;    <h1>我的第一个Vue应用</h1>&ndash;&gt;-->
<!--    <p>当前点赞数：{{ likes }}</p>-->
<!--    <button @click="likes++">点赞{{ likes }}</button>-->
<!--    <p v-if="likes>=10">哇，十连赞达成！</p>-->
<!--    <input type="text" v-model="visitorName">-->
<!--    <p>剩余点赞数：{{ remainingLikes }}</p>-->
<!--    <ul>-->
<!--      <li v-for="message in messages">{{ message }}</li>-->
<!--    </ul>-->
<!--    <input type="text" v-model="newMessage"></input>-->
<!--    <button @click="submitMessage">提交</button>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div class="container">
    <h1>欢迎，{{ visitorName }} 的 Vue 应用 🎉</h1>
    <div class="input-group">
      <label>你的名字：</label>
      <input type="text" v-model="visitorName" placeholder="输入你的名字">
    </div>

    <!--    <div class="card likes-section">-->
    <!--      <p class="score">当前点赞数：{{ likes }}</p>-->
    <!--      <button class="btn-primary" @click="likes++">点赞 👍</button>-->

    <!--      <p class="celebrate" v-if="likes >= 10">哇，十连赞达成！🎉🎉🎉</p>-->
    <!--      <p class="hint" v-if="likes < 10">距离十连赞还差: {{ remainingLikes }} 次</p>-->
    <!--    </div>-->
    <LikeWidget
        :currentLikes="likes"
        @add-like="handleLikeEvent"
    />

    <!--    <div class="card messages-section">-->
    <!--      <h2>📝 留言板</h2>-->

    <!--      <ul class="message-list">-->
    <!--        <li v-for="(message, index) in messages"-->
    <!--            :key="index"-->
    <!--            @click="goToDetail(index)"-->
    <!--            class="clickable-item"-->
    <!--        >-->
    <!--          {{ message }}-->
    <!--        </li>-->
    <!--      </ul>-->

    <!--      <div class="input-group">-->
    <!--        <input-->
    <!--            type="text"-->
    <!--            v-model="newMessage"-->
    <!--            placeholder="写下你的留言..."-->
    <!--            @keyup.enter="submitMessage"-->
    <!--        >-->
    <!--        <button class="btn-success" @click="submitMessage">发布留言</button>-->
    <!--      </div>-->
    <!--    </div>-->

    <MessageBoard
        :messages="messages"
        @add-message="handleAddMessage"
        @click-message="handleGoToDetail"
    />
  </div>
</template>

<!--添加样式作用域-->
<!--<style scoped>-->
<!--.container {-->
<!--  max-width: 600px;-->
<!--  margin: 40px auto;-->
<!--  font-family: 'Helvetica Neue', Arial, sans-serif;-->
<!--  color: #333;-->
<!--}-->

<!--h1 {-->
<!--  text-align: center;-->
<!--  color: #42b883; /* Vue 官方绿 */-->
<!--}-->

<!--.card {-->
<!--  border: 1px solid #eee;-->
<!--  border-radius: 8px;-->
<!--  padding: 20px;-->
<!--  margin-top: 20px;-->
<!--  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);-->
<!--  background: #fff;-->
<!--}-->

<!--.likes-section {-->
<!--  text-align: center;-->
<!--}-->

<!--.score {-->
<!--  font-size: 1.2rem;-->
<!--  font-weight: bold;-->
<!--}-->

<!--.celebrate {-->
<!--  color: #e74c3c;-->
<!--  font-weight: bold;-->
<!--  margin-top: 15px;-->
<!--}-->

<!--.hint {-->
<!--  color: #7f8c8d;-->
<!--  font-size: 0.9rem;-->
<!--}-->

<!--.message-list {-->
<!--  text-align: left;-->
<!--  background: #f9f9f9;-->
<!--  padding: 15px 15px 15px 35px;-->
<!--  border-radius: 4px;-->
<!--}-->

<!--.message-list li {-->
<!--  margin-bottom: 10px;-->
<!--  line-height: 1.5;-->
<!--}-->

<!--.input-group {-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--  gap: 10px;-->
<!--  margin-top: 15px;-->
<!--  align-items: center;-->
<!--}-->

<!--input[type="text"] {-->
<!--  padding: 8px 12px;-->
<!--  border: 1px solid #ccc;-->
<!--  border-radius: 4px;-->
<!--  font-size: 1rem;-->
<!--  flex: 1; /* 让输入框自动占据剩余空间 */-->
<!--}-->

<!--button {-->
<!--  padding: 10px 20px;-->
<!--  border: none;-->
<!--  border-radius: 4px;-->
<!--  font-size: 1rem;-->
<!--  cursor: pointer;-->
<!--  transition: opacity 0.2s;-->
<!--  color: white;-->
<!--  font-weight: bold;-->
<!--}-->

<!--button:hover {-->
<!--  opacity: 0.8;-->
<!--}-->

<!--.btn-primary {-->
<!--  background-color: #3498db;-->
<!--}-->

<!--.btn-success {-->
<!--  background-color: #42b883;-->
<!--}-->

<!--.clickable-item {-->
<!--  cursor: pointer;-->
<!--  transition: background 0.2s;-->
<!--}-->

<!--.clickable-item:hover {-->
<!--  background: #e9e9e9;-->
<!--}-->
<!--</style>-->

<style scoped>
/* 首页只保留最外层的布局排版样式，具体的卡片样式都在积木自己内部 */
.container {
  max-width: 600px;
  margin: 40px auto;
  font-family: sans-serif;
  color: #333;
}

h1 {
  text-align: center;
  color: #42b883;
}

.input-group {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 15px;
  align-items: center;
}

input[type="text"] {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  flex: 1;
  max-width: 300px;
}
</style>