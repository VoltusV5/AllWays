<template>
  <header class="header">
    <div class="logo">
      <img src="C:/Visual_Studio/WEB/AllWays/AW-VueJs/AllWays-vue/src/assets/images/logo-big.png" alt="AllWays Logo">
    </div>

    <div class="user">
      <img src="C:/Visual_Studio/WEB/AllWays/AW-VueJs/AllWays-vue/src/assets/images/icon.png" alt="User Icon">
    </div>
    <nav></nav>
  </header>
</template>

<script>
  export default {
    name: 'Header'
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