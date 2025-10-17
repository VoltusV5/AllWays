<template>
  <div class="enter-password">
    <h2>Введите пароль</h2>
    
    <div class="account-info">
      Для аккаунта <span class="email">mail.mail@gmail.com</span>
    </div>

    <div class="input-wrapper">
      <input :type="showPassword ? 'text' : 'password'" v-model="password" 
        placeholder="Введите пароль" />
          
      <button type="button" class="toggle-password" @click="showPassword = !showPassword">
        {{ showPassword ? '🙈' : '👁️' }}
      </button>
    </div>

    <button class="login-button" @click="login">Войти</button>
    
    <div class="forgot-password" @click="forgotPassword">
      Не помню пароль
    </div>
  </div>
</template>

<script>
export default {
  name: "EnterPassword",
  data() {
    return {
      password: "",
      showPassword: false,
    };
  },
  methods: {
    login() {
      if (!this.password) {
        alert("Введите пароль!");
        return;
      }
      alert(`Пароль введён: ${this.password}`);
    },
    forgotPassword() {
      alert("Функция восстановления пароля");
    },
  },
};
</script>

<style scoped>
.enter-password {
  width: 100%;
}

h2 {
  color: #fff;
  text-align: center;
  margin-bottom: 20px;
}

.account-info {
  margin-top: 10px;
  margin-bottom: 20px;
  font-size: 14px;
  color: #bbb;
  text-align: center;
}

.account-info .email {
  font-weight: bold;
  color: #fff;
}

.input-wrapper {
  position: relative;
  margin: 20px 0;
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

.toggle-password {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: #aaa;
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
  margin-top: 15px;
}

.login-button:hover {
  background: #c56e32;
}

.forgot-password {
  margin-top: 15px;
  font-size: 14px;
  color: #aaa;
  cursor: pointer;
  text-align: center;
}

.forgot-password:hover {
  color: #fff;
}
</style>