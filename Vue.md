

Vue 官方最推荐的项目创建方式是使用基于 **Vite** 的工具。它不仅配置简单，而且启动和热更新的速度惊人 ⚡️。

不过，在我们在终端（命令行）里敲下第一行创建代码之前，我们需要确保你的电脑上已经准备好了地基——**Node.js**（一个能让 JavaScript 在浏览器之外运行的环境）。

你可以打开你的终端（Windows 用户可以打开 PowerShell 或 cmd，Mac 用户打开终端 Terminal），输入以下命令来检查：



~~~html
node -v

markdown_content = """# 📝 Vue 3 基础入门与 Git 排障实操笔记

## 1. 项目搭建与启动 🚀
为了兼容当前的 Node.js 版本 (v20.17.0)，我们使用了 Vite 5 来创建纯净的 Vue 3 项目：
```bash
# 创建项目 (选择 Vue -> JavaScript)
npm create vite@5

# 进入项目并启动
cd my-vue-app
npm install
npm run dev
~~~

## 2. Vue 核心概念与指令 (我们的武器库) 🛠️

Vue 的单文件组件 (`.vue`) 通常包含三个部分：`<script setup>` (大脑/逻辑)、`<template>` (骨架/结构) 和 `<style scoped>` (外衣/样式)。

- **`ref` (响应式数据)**：
  - **作用**：把普通数据包装成 Vue 会自动追踪的变量。数据一变，页面自动更新。
  - **语法**：`import { ref } from 'vue'`
  - **注意**：在 JavaScript 中读取或修改它时，必须加 `.value`；在 `<template>` 模板中直接使用即可。
- **`{{ }}` (插值语法)**：
  - **作用**：在 HTML 页面中直接显示 JavaScript 变量的值。
- **`@click` (事件绑定)**：
  - **作用**：监听用户的点击动作并触发相应的代码（例如 `likes++` 或调用一个函数）。
- **`v-if` (条件渲染)**：
  - **作用**：根据条件判断，决定一个 HTML 元素是否在页面上显示（例如满 10 赞显示彩蛋）。
- **`v-model` (双向数据绑定)**：
  - **作用**：在表单输入框 `<input>` 和变量之间建立双向同步。用户输入会改变变量，变量改变也会更新输入框。
- **`computed` (计算属性)**：
  - **作用**：根据已有的响应式数据，自动推导、计算出新的数据（例如计算距离目标还差几个赞）。它会智能缓存，只在依赖的数据变化时才重新计算。
- **`v-for` (列表渲染)**：
  - **作用**：遍历一个数组，自动循环生成对应的 HTML 列表项。
  - **语法**：`v-for="item in array"`

## 3. 核心案例代码整合 (互动点赞与留言板) 💻

```html
<script setup>
import { ref, computed } from 'vue'

// 1. 响应式变量
const likes = ref(0)
const visitorName = ref('神秘嘉宾')
const newMessage = ref('')
const messages = ref([
  'Vue 真好玩！',
  '我也来点个赞~'
])

// 2. 计算属性
const remainingLikes = computed(() => 10 - likes.value)

// 3. 处理函数 (待完善追加数组的功能)
function submitMessage() {
  // TODO: 将 newMessage.value 追加到 messages.value 数组中
  newMessage.value = ''
}
</script>

<template>
  <div class="container">
    <h1>欢迎，{{ visitorName }} 的 Vue 应用 🎉</h1>
    <input type="text" v-model="visitorName">

    <p>当前点赞数：{{ likes }}</p>
    <button @click="likes++">点赞 {{ likes }}</button>
    <p v-if="likes >= 10">哇，十连赞达成！🎉</p>
    <p v-if="likes < 10">距离十连赞还差: {{ remainingLikes }} 次</p>

    <hr>

    <ul>
      <li v-for="message in messages">{{ message }}</li>
    </ul>
    <input type="text" v-model="newMessage" placeholder="写下你的留言...">
    <button @click="submitMessage">发布留言</button>
  </div>
</template>
```

