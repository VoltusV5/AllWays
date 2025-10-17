<template>
  <div class="social-login-buttons">
    <a href="#" class="social-button">
      <img src="@/assets/images/yandex.png" alt="Yandex">
    </a>
    <a href="#" class="social-button">
      <img src="@/assets/images/VK.png" alt="VK">
    </a>
    <a href="#" class="social-button">
      <img src="@/assets/images/mail.ru.png" alt="Mail.ru">
    </a>
    <a href="#" class="social-button">
      <img src="@/assets/images/Odnoklassniki.png" alt="Odnoklassniki">
    </a>
    <a href="#" class="social-button">
      <img src="@/assets/images/google.png" alt="Google">
    </a>
  </div>
</template>

<script>
import ArrowBack from '@/ui/ArrowBack.vue'

export default {
  name: 'SocialLoginButtons'
}
</script>

<style scoped>
.social-login-buttons {
  width: 310px;
  margin: 15px auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.social-button {
  width: 54px;
  height: 37px;
  background: #D9D9D9;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.social-button img {
  width: 24px;
  height: 24px;
}

.social-button:hover {
  opacity: 0.9;
}
</style>