<template>
  <div class="arrow-back">
    <button @click="goToMainPage" class="back-button">
      <img src="@/assets/images/ArrowBack.png" alt="Arrow Back">
    </button>    
  </div>
</template>

<script>
export default {
    name: 'ArrowBack',
    methods: {
        goToMainPage() {
            try {
                this.$router.go(-1);
            } catch (error) {
                console.error('Navigation error:', error);
            }
        }
    }
}
</script>

<style scoped>
.arrow-back {
    display: inline-block;
    z-index: 1;
    position: relative; 
}

.arrow-back img {
  width: 15px;
  height: 15px;
}

.back-button {
    border: 0;
    border-radius: 14px;
    width: 34px;
    height: 30px;
    background: rgba(0, 0, 0, 0.6);
    cursor: pointer;
    padding: 0;
}

.back-button:hover {
    opacity: 1;
    background-color: rgba(0, 0, 0, 0.8);
    transform: scale(1.05);
}

.back-button img {
    width: 34px;
    height: 30px;
    object-fit: contain;
}
</style>