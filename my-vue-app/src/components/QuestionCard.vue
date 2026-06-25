<script setup>
//接收固定的数据属性
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  score: {
    type: Number,
    default: 5//默认分数5分
  }
})
</script>

<template>
  <div class="exam-card">
    <div class="card-header">
      <h3 class="title">{{ title }}</h3>
      <span class="score">满分：{{ score }}</span>
    </div>
    <div class="card-body">
      <slot>
        <p style="color: #999;">请提供题目内容。。。</p>
      </slot>
    </div>
  </div>
</template>

<style scoped>
.exam-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  margin-bottom: 20px;
  overflow: hidden;
}

.card-header {
  background-color: #f8f9fa;
  padding: 12px 20px;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  margin: 0;
  font-size: 1.1rem;
  color: #2c3e50;
}

.score {
  font-weight: bold;
  color: #e74c3c;
}

.card-body {
  padding: 20px;
}
</style>