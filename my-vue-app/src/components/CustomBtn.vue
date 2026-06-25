<script setup>
</script>

<template>
  <button class="my-custom-btn">
    <!-- 按钮里挖了个坑。无论是纯文字，还是带图标的 HTML，都能往里塞 -->
    <slot>默认按钮</slot>
  </button>
</template>

<style scoped>
.my-custom-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, #6e8efb, #a777e3); /* 炫酷渐变色 */
  color: white;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.1s, opacity 0.2s;

  /* Flex 布局能让插槽里的 图标 和 文字 完美居中对齐 */
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.my-custom-btn:hover {
  opacity: 0.9;
}

.my-custom-btn:active {
  transform: scale(0.95); /* 点击时微微缩小的反馈 */
}
</style>