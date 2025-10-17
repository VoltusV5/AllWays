<template>
  <div class="authorization-page-password">
    <div class="auth-container">
      <AuthHeader />
      <EnterPassword :email="userEmail" @login-success="handleLoginSuccess" />
    </div>
  </div>
</template>

<script>
import AuthHeader from "@/components/AuthorizationPagePassword/AuthHeader.vue"
import EnterPassword from '@/components/AuthorizationPagePassword/EnterPassword.vue'

export default {
  name: "AuthorizationPagePassword",
  components: {
    AuthHeader,
    EnterPassword
  },
  data() {
    return {
      userEmail: ''
    }
  },
  mounted() {
    this.userEmail = this.$route.query.email || 'mail.mail@gmail.com';
  },
  methods: {
    handleLoginSuccess() {
      this.$router.push('/');
    },

    handleLoginFail(errorMessage) {
      alert(errorMessage);
    }
  }
};

</script>

<style scoped>
.authorization-page-password {
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