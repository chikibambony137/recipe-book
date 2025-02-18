<script>
  export default {
    methods: {
      goToLogin() {
        this.$router.push('/login')
      }
    }
  }
</script>

<template>
  <div>
    <router-view></router-view>
    <h1 v-if="$route.path === '/'">Добро пожаловать!</h1>
    <button v-if="$route.path === '/' " @click="goToLogin">Войти</button>
  </div>
</template>

<style scoped>
  
</style>
