<script setup>
import {computed} from "vue";

// 1. 接收父组件传来的数据 (Props Down)
// defineProps 告诉 Vue：我这个小积木需要外界给我提供一个叫 currentLikes 的数字才能工作
const props = defineProps({
  currentLikes: {
    type: Number,
    required: true
  }
})
// 2. 向父组件发送信号的发射器 (Events Up)
// defineEmits 告诉 Vue：我这个小积木会向外发射一个叫 'add-like' 的事件
const emit = defineEmits(['add-like'])

const remainingLikes = computed(() => 10 - props.currentLikes)

function handleLikeClick() {
  emit('add-like')
}
</script>

<template>
  <div class="card likes-section">
    <p class="score">当前点赞数：{{ currentLikes }}</p>

    <button class="btn-primary" @click="handleLikeClick">点赞 👍</button>

    <p class="celebrate" v-if="currentLikes >= 10">哇，十连赞达成！🎉🎉🎉</p>
    <p class="hint" v-if="currentLikes < 10">距离十连赞还差: {{ remainingLikes }} 次</p>
  </div>
</template>

<style scoped>
/* 这里只保留点赞卡片专属的样式 */
.card {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 20px;
  margin-top: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  background: #fff;
}

.likes-section {
  text-align: center;
}

.score {
  font-size: 1.2rem;
  font-weight: bold;
}

.celebrate {
  color: #e74c3c;
  font-weight: bold;
  margin-top: 15px;
}

.hint {
  color: #7f8c8d;
  font-size: 0.9rem;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  color: white;
  font-weight: bold;
  background-color: #3498db;
}
</style>