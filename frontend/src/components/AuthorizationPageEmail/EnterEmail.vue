<template>
  <div class="enter-email">
    <ArrowBack />
    <img src="@/assets/images/logo-big.png" alt="AllWays Logo" class="logo">
    <h2>Войдите, чтобы покупать билеты и сохранять поездки</h2>
    
    <div class="input-wrapper">
      <input 
        type="email" 
        v-model="email" 
        placeholder="mail.mail@gmail.com"
        @input="handleInput"
      />
      <button 
        v-if="email" 
        class="clear-button" 
        @click="clearEmail"
      >
        ✕
      </button>
    </div>

    <button class="login-button" @click="continueToPassword">Войти</button>
    
    <SocialLoginButtons />
    
    <div class="create-account-wrapper">
      <div class="create-account" @click="createAccount">Создать аккаунт</div>
    </div>
  </div>
</template>

<script>
import ArrowBack from '@/ui/ArrowBack.vue';
import SocialLoginButtons from '@/ui/SocialLoginButtons.vue';

export default {
  name: "EnterEmail",
  components: {
    ArrowBack,
    SocialLoginButtons
  },
  data() {
    return {
      email: "",
    };
  },
  methods: {
    continueToPassword() {
      if (!this.email) {
        alert("Введите email!");
        return;
      }
      this.$emit('email-entered', this.email);
    },
    createAccount() {
      this.$router.push('/registration');
    },
    clearEmail() {
      this.email = "";
    },
    handleInput() {
    }
  },
};
</script>

<style scoped>
.enter-email {
  width: 100%;
  padding: 0 16px;
  position: relative;
}

.logo {
  display: block;
  width: 148px;
  height: 46px;
  margin: 20px auto 40px;
}

h2 {
  color: #fff;
  text-align: center;
  margin-bottom: 40px;
  font-size: 16px;
  font-weight: normal;
  line-height: 1.4;
}

.input-wrapper {
  position: relative;
  margin: 30px 0 10px;
}

.input-wrapper input {
  width: 100%;
  padding: 12px 40px 12px 12px;
  border-radius: 6px;
  border: 1px solid #444;
  background: #1e1e1e;
  color: #fff;
  font-size: 14px;
  box-sizing: border-box;
}

.clear-button {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: #aaa;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.clear-button:hover {
  color: #fff;
}

.login-button {
  width: 100%;
  padding: 12px;
  border-radius: 6px;
  border: none;
  background: #d97b3c;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
}

.login-button:hover {
  background: #c56e32;
}

.create-account-wrapper {
  width: 310px;
  height: 37px;
  background: #606060;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 15px auto 0;
}

.create-account {
  font-size: 14px;
  color: #aaa;
  cursor: pointer;
  text-align: center;
}

.create-account:hover {
  color: #fff;
}
</style>