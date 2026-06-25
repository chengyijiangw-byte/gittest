<script setup>

</script>

<template>
  <div class="shadow-card">
    <slot>
      <!--    兜底内容，如果找不到插槽内容，就会显示这里-->
      <p style="color: #999;text-align: center;">卡片里面空空如也......</p>
    </slot>
  </div>
</template>


//border-radius: 12px; 圆角：让卡片的四个角变成弧度为 12 像素的圆角。相比于尖锐的直角，圆角会让界面看起来更加柔和、现代。
//padding: 24px; 内部填充：让卡片内容区域有 24 个像素的填充，这样内容就不会贴着卡片的边缘。
//border: 1px solid #f0f0f0; 卡片边框：让卡片有 1 个像素的边框，并使用浅灰色作为边框颜色。
// transition: box-shadow 0.3s ease, transform 0.3s ease; 卡片阴影和动画：让卡片有阴影效果，当卡片的阴影或位置发生改变时，不要瞬间突变，而是用 0.3 秒的时间平滑过渡过去”。ease 表示动画速度是“缓入缓出”（开头和结尾慢，中间快），非常符合自然物理规律。
<style scoped>
.shadow-card {
  background: #eaefec;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
  border: 1px solid #f0f0f0;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.shadow-card:hover {
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
  transform: translateY(-10px);
}
</style>