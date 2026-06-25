<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// useRoute 用于获取当前网址上的信息；useRouter 用于执行跳转操作
const route = useRoute()
const router = useRouter()

// 1. 从网址上抓取刚刚传过来的 id
const messageId = route.params.id

// 2. 准备一个变量来存放留言内容
const messageContent = ref('加载中...')

// 3. 从 localStorage 读取所有留言，并根据 id 找到对应的那一条
const savedMessages = localStorage.getItem('my_vue_messages')
if (savedMessages) {
  const messagesArray = JSON.parse(savedMessages)
  // 根据索引提取对应的内容
  messageContent.value = messagesArray[messageId]
}
</script>

<template>
  <div class="container">
    <h2>📄 留言详情 (编号: {{ messageId }})</h2>

    <div class="message-card">
      <p>{{ messageContent }}</p>
    </div>

    <button class="back-btn" @click="router.back()">⬅️ 返回留言板</button>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 40px auto;
  text-align: center;
}

.message-card {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin: 20px 0;
  font-size: 1.2rem;
  color: #333;
}

.back-btn {
  padding: 10px 20px;
  background-color: #95a5a6;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.back-btn:hover {
  background-color: #7f8c8d;
}
</style>