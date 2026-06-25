<script setup>
import SimpleDialogWidget from "../components/SimpleDialogWidget.vue";
import ShadowCard from "../components/ShadowCard.vue";

import {ref} from "vue";
import CustomBtn from "../components/CustomBtn.vue";

const userName = ref('')
</script>

<template>
  <div style="padding: 40px;font-family: sans-serif;">
    <h1>测试单插槽</h1>
    <SimpleDialogWidget>
      <form style="background: #f9f9f9; padding: 15px; border-radius: 4px;">
        <h4 style="margin-top: 0;">请填写资料</h4>
        <label>姓名：</label>
        <input type="text" v-model="userName" placeholder="输入姓名"/>
        <p v-if="userName">你好呀，{{ userName }}！</p>
      </form>
    </SimpleDialogWidget>
    <ShadowCard>
      <h4>通用卡片测试</h4>
    </ShadowCard>

    <CustomBtn>
      <button>按钮</button>
    </CustomBtn>
  </div>
</template>

<style scoped>

</style>