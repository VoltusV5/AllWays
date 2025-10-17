<template>
  <div class="registration-page">
    <div class="auth-container">
      <ArrowBack />
      <img src="@/assets/images/logo-big.png" alt="AllWays Logo" class="logo">
      <h2>Создайте аккаунт, чтобы покупать билеты и сохранять поездки</h2>
      
      <!-- Логин -->
      <div class="input-wrapper">
        <input 
          type="text" 
          v-model="login" 
          placeholder="Введите логин"
          @input="handleInput"
        />
        <button 
          v-if="login" 
          class="clear-button" 
          @click="clearLogin"
        >
          ✕
        </button>
      </div>

        <!-- Email -->
      <div class="input-wrapper">
        <input 
          type="email" 
          v-model="email" 
          placeholder="Введите почту"
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

      <!-- Пароль -->
      <div class="input-wrapper">
        <input 
          :type="showPassword ? 'text' : 'password'" 
          v-model="password" 
          placeholder="Введите пароль"
        />
        <button 
          type="button" 
          class="toggle-password" 
          @click="showPassword = !showPassword"
        >
          {{ showPassword ? '🙈' : '👁️' }}
        </button>
      </div>

      <!-- Подтверждение пароля -->
      <div class="input-wrapper">
        <input 
          :type="showConfirmPassword ? 'text' : 'password'" 
          v-model="confirmPassword" 
          placeholder="Повторите пароль"
        />
        <button 
          type="button" 
          class="toggle-password" 
          @click="showConfirmPassword = !showConfirmPassword"
        >
          {{ showConfirmPassword ? '🙈' : '👁️' }}
        </button>
      </div>

      <!-- Политика конфиденциальности -->
      <div class="privacy-policy">
        <input 
          type="checkbox" 
          v-model="acceptPolicy" 
          id="privacy-policy"
        />
        <label for="privacy-policy">Я принимаю политику конфиденциальности</label>
      </div>
      
      <!-- Кнопка регистрации -->
      <button class="register-button" @click="register">Создать аккаунт</button>
      
      <!-- Социальная авторизация -->
      <SocialLoginButtons />
      
      <!-- Ссылка на страницу входа -->
      <div class="login-link-wrapper">
        <div class="login-link" @click="goToLogin">Уже есть аккаунт</div>
      </div>
    </div>
  </div>
</template>

<script>
import ArrowBack from '@/ui/ArrowBack.vue';
import SocialLoginButtons from '@/ui/SocialLoginButtons.vue';
import axios from 'axios';
import { getCSRFToken } from '@/utils/csrf';

export default {
  name: "RegistrationPage",
  components: {
    ArrowBack,
    SocialLoginButtons
  },
  data() {
    return {
      login: "",
      email: "",
      password: "",
      confirmPassword: "",
      showPassword: false,
      showConfirmPassword: false,
      acceptPolicy: false
    };
  },
  methods: {
    async register() {
      // Проверка обязательных полей
      if (!this.login || !this.email || !this.password || !this.confirmPassword) {
        alert("Заполните все поля!");
        return;
      }

      // Проверка совпадения паролей
      if (this.password !== this.confirmPassword) {
        alert("Пароли не совпадают!");
        return;
      }

      // Проверка принятия политики
      if (!this.acceptPolicy) {
        alert("Пожалуйста, примите политику конфиденциальности!");
        return;
      }

      const csrfToken = getCSRFToken();

      try {
        const response = await axios.post('/api/users/register/', {
          email: this.email,
          password: this.password,
          username: this.login,
        }, {
          headers: {
            'X-CSRFToken': csrfToken // Добавляем CSRF токен в заголовок
          }
        });

        if (response.status === 201) {
          alert("Регистрация успешна!");
          this.$router.push('/login');
        }
      } catch (error) {
        console.error("Ошибка регистрации:", error.response.data);
        if (error.response && error.response.data) {
          alert(error.response.data.error || 'Ошибка при регистрации');
        } else {
          alert('Что-то пошло не так, попробуйте снова.');
        }
      }
    },
    clearLogin() {
      this.login = "";
    },
    clearEmail() {
      this.email = "";
    },
    handleInput() {
      // Optional: Add any input handling logic if needed
    },
    goToLogin() {
      this.$router.push('/authorization-email');
    }
  }
};
</script>

<style scoped>
.registration-page {
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

.logo {
  display: block;
  width: 148px;
  height: 46px;
  margin: 20px auto 40px;
}

h2 {
  color: #606060;
  text-align: center;
  margin-bottom: 40px;
  font-size: 16px;
  font-weight: normal;
  line-height: 1.4;
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
  background: #D9D9D9;
  color: #fff;
  font-size: 14px;
  box-sizing: border-box;
}

.input-wrapper input::placeholder {
  color: #606060;
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

.privacy-policy {
  display: flex;
  align-items: center;
  margin: 20px 0;
  color: #606060;
  font-size: 14px;
}

.privacy-policy input {
  margin-right: 10px;
}

.privacy-policy label {
  cursor: pointer;
}

.register-button {
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

.register-button:hover {
  background: #c56e32;
}

.login-link-wrapper {
  width: 100%;
  height: 37px;
  background: #606060;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 15px auto 0;
}

.login-link {
  font-size: 14px;
  color: #fff;
  cursor: pointer;
  text-align: center;
}

.login-link:hover {
  opacity: 0.9;
}
</style>