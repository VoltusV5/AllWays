<template>
  <div class="authorization-page-email">
    <div class="auth-container">
      <AuthHeader />
      <EnterEmail @email-entered="handleEmailEntered" />
    </div>
  </div>
</template>

<script>
    // import AuthHeader from "@/components/AuthorizationPageEmail/AuthHeader.vue"
import axios from 'axios';
import EnterEmail from '@/components/AuthorizationPageEmail/EnterEmail.vue'

export default {
    name: "AuthorizationPageEmail",
    components: {
        // AuthHeader,
        EnterEmail
    },
    methods: {
      async handleEmailEntered(email) {
        try {
          const response = await axios.post('/api/users/check-email/', { email });

          if (response.status === 200 && response.data.exists) {
            this.$router.push({
              path: '/authorization-password',
              query: { email: email }
            });
          } else {
            alert('Email не найден. Пожалуйста, зарегистрируйтесь.');
          }
          } catch (error) {
            console.error("Error while checking email:", error)
            alert("Ошибка при проверке email. Попробуйте снова.")
          }
        }
      },
      handleEmailEntered(email) {
        // Переходим на страницу ввода пароля, передавая email
        this.$router.push({
          path: '/authorization-password',
          query: { email: email }
        });
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