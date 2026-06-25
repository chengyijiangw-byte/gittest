<script setup>
import {ref} from 'vue'

// 1. 接收父组件传来的留言列表 (Props Down)
const props = defineProps({
  messages: {
    type: Array,
    required: true
  }
})

// 2. 定义要向外发射的事件 (Events Up)
// 这里我们需要两个事件：一个是发布新留言，一个是点击某条留言跳转
const emit = defineEmits(['add-message', 'click-message'])

// 3. 封装组件内部的私有状态
// 这个 newMessage 只是输入框里的临时文字，父组件根本不需要管它，放在子组件里最合适！
const newMessage = ref('')

function submit() {
  if (newMessage.value.trim() !== '') {
    // 【新知识点】：在发射事件的同时，把输入的内容作为第二个参数“快递”给父组件
    emit('add-message', newMessage.value)
    newMessage.value = '' // 清空自己的输入框
  }
}
</script>

<template>
  <div class="card messages-section">
    <h2>📝 留言板</h2>

    <ul class="message-list">
      <li
          v-for="(message, index) in messages"
          :key="index"
          @click="emit('click-message', index)"
          class="clickable-item"
      >
        {{ message }}
      </li>
    </ul>

    <div class="input-group">
      <input
          type="text"
          v-model="newMessage"
          placeholder="写下你的留言..."
          @keyup.enter="submit"
      >
      <button class="btn-success" @click="submit">发布留言</button>
    </div>
  </div>
</template>

<style scoped>
/* 留言板专属的样式搬到这里 */
.card {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 20px;
  margin-top: 20px;
  background: #fff;
}

.message-list {
  text-align: left;
  background: #f9f9f9;
  padding: 15px 15px 15px 35px;
  border-radius: 4px;
}

.message-list li {
  margin-bottom: 10px;
  line-height: 1.5;
}

.clickable-item {
  cursor: pointer;
  transition: background 0.2s;
}

.clickable-item:hover {
  background: #e9e9e9;
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
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  color: white;
  font-weight: bold;
}

.btn-success {
  background-color: #42b883;
}
</style>