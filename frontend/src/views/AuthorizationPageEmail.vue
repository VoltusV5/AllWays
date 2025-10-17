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
    import EnterEmail from '@/components/AuthorizationPageEmail/EnterEmail.vue'
   
    export default {
        name: "AuthorizationPageEmail",
        components: {
            // AuthHeader,
            EnterEmail
        },
        methods: {
          handleEmailEntered(email) {
            // Переходим на страницу ввода пароля, передавая email
            this.$router.push({
              path: '/authorization-password',
              query: { email: email }
            });
          }
        }
    }
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