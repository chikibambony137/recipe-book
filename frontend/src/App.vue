<script setup>
  import LoginForm from './components/LoginForm.vue';
</script>

<template>
  <div class="loginForm">
      <LoginForm/>
  </div>
  
</template>

<style scoped>
  .loginForm {
    background-color: #1F42AE;
    width: 350px;
    height: 500px;
    border-radius: 20px;
    position: relative;
    left: 50%;
    top: 15%;
  }
</style>
