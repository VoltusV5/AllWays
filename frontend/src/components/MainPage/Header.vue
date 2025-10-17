<template>
  <header class="header">
    <div class="logo">
      <button @click="goToHome">
        <img src="@/assets/images/logo-big.png" alt="AllWays Logo">
      </button>
    </div>

    <div class="user">
      <button @click="goToAuthorizationPage">
        <img src="@/assets/images/icon.png" alt="User Icon">
      </button>
    </div>
  </header>
</template>

<script>
  export default {
    name: 'Header',
    methods: {
      goToHome() {
        try {
          this.$router.push('/');
        } catch (error) {
          console.error('Navigation error:', error);
        }
      },
      goToAuthorizationPage() {
        try {
          // Теперь переходим на страницу ввода email
          this.$router.push('/authorization-email');
        } catch (error) {
          console.error('Navigation error:', error);
        }
      }
    },
    errorCaptured(err, instance, info) {
      console.error('Error captured in Header:', err, info);
      return false;
    }
  }
</script>

<style scoped>
  header {
    background-color: none;
    color: #000000;
    padding: 24px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo img {
    position: absolute;
    width: 148px;
    height: 46px;
    left: 5px;
    top: 5px;
  }

  .user img {
    position: absolute;
    width: 46px;
    height: 46px;
    right: 10px;
    top: 5px;
  }
</style>