<script setup>
import {ref} from 'vue'
import QuestionCard from '../components/QuestionCard.vue'

// 存放学生答题的数据
const answer1 = ref('')
const answer2 = ref('')
</script>

<template>
  <div class="container">
    <h1>📝 期末考试系统</h1>
    <hr>

    <QuestionCard title="第一题：基础概念" :score="10">
      <p class="question-text">请简述你对响应式编程的理解：</p>
      <textarea
          v-model="answer1"
          rows="4"
          placeholder="在此输入你的答案..."
      ></textarea>
    </QuestionCard>

    <QuestionCard title="第二题：Python 编程实战" :score="20">
      <p class="question-text">
        请编写一个 Python 函数，使用 <code>random.uniform</code> 生成一个指定范围内的随机浮点数。
      </p>
      <div class="code-editor-mock">
        <textarea
            v-model="answer2"
            rows="6"
            placeholder="def generate_random(min_val, max_val):&#10;    # 写下你的 Python 代码"
            style="font-family: monospace; background: #282c34; color: #abb2bf;"
        ></textarea>
      </div>
    </QuestionCard>

    <div class="action-bar">
      <button class="btn-submit">交 卷</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 700px;
  margin: 40px auto;
  font-family: sans-serif;
}

h1 {
  text-align: center;
  color: #2c3e50;
}

.question-text {
  font-size: 1.05rem;
  margin-bottom: 15px;
  color: #333;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; /* 确保 padding 不会撑破容器 */
  resize: vertical;
}

.action-bar {
  text-align: center;
  margin-top: 30px;
}

.btn-submit {
  background-color: #4CAF50;
  color: white;
  padding: 12px 30px;
  border: none;
  border-radius: 4px;
  font-size: 1.2rem;
  cursor: pointer;
  font-weight: bold;
}

.btn-submit:hover {
  background-color: #45a049;
}
</style>