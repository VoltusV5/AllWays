<template>
  <div class="auth-header">
    <ArrowBack />
    <img src="@/assets/images/key.png" alt="Key" class="key-image">
  </div>
</template>

<script>
  import ArrowBack from '@/ui/ArrowBack.vue';

  export default {
    name: 'AuthHeader',
    components: {
      ArrowBack
    }
  }
</script>

<style scoped>
.auth-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px;
  position: relative; /* для абсолютного позиционирования дочерних элементов */
  min-height: 200px; /* минимальная высота для центрирования */
}

.key-image {
  width: 143px;
  height: 143px;
  opacity: 60%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* центрирует точно по середине */
}
</style>