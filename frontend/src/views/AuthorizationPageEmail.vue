<template>
  <div class="authorization-page-email">
    <div class="auth-container">
      <AuthHeader />
      <EnterEmail @email-entered="handleEmailEntered" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import EnterEmail from '@/components/AuthorizationPageEmail/EnterEmail.vue';
import { getCSRFToken } from '@/utils/csrf';

export default {
  name: "AuthorizationPageEmail",
  components: {
    EnterEmail
  },
  methods: {
    async handleEmailEntered(email) {
      try {
        const csrfToken = getCSRFToken();
        const response = await axios.post(
          '/api/users/check-email/',
          { email },
          {
            headers: {
              'X-CSRFToken': csrfToken
            }
          }
        );

        if (response.status === 200 && response.data.exists) {
          this.$router.push({
            path: '/authorization-password',
            query: { email }
          });
        } else {
          alert('Email не найден. Пожалуйста, зарегистрируйтесь.');
        }
      } catch (error) {
        console.error("Ошибка при проверке email:", error);
        if (error.response && error.response.status === 403) {
          alert("Ошибка CSRF. Пожалуйста, обновите страницу и попробуйте снова.");
        } else if (error.response && error.response.data.error) {
          alert(error.response.data.error);
        } else {
          alert("Ошибка при проверке email. Попробуйте снова.");
        }
      }
    }
  }
};
</script>

<style scoped>
.authorization-page-email {
  background-color: #232323;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth-container {
  width: 100%;
  max-width: 375px;
  padding: 0 16px;
}
</style>