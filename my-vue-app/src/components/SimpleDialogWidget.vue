<script setup>

</script>

<template>
  <div class="dialog" style="border: 1px solid black; padding: 20px;">
    <h3>固定的标题</h3>

    <!-- 核心：挖了一个坑 -->
    <div class="body-area" style="border: 1px dashed red; margin: 10px 0;">
      <slot></slot>
    </div>

    <button>固定的按钮</button>
  </div>
</template>

<style scoped>

</style>