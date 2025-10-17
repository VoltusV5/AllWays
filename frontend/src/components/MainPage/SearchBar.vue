<template>
  <div class="search-container">
    <div class="bottom-panel"></div>
    <div class="arrow-indicator">
      <img src="@/assets/images/arrow.png" alt="Индикатор">
    </div>
    
    <div class="search-bar">
      <div class="search-input">
        <img src="@/assets/images/logo-small.png" alt="Logo" class="search-logo">
        <input type="text" placeholder="Поиск и выбор мест" class="search-field">
        <img src="@/assets/images/search_magnifier_1.png" alt="Поиск" class="search-icon">
      </div>
      
      <div class="bookmark-button">
        <img src="@/assets/images/bookmark.png" alt="Закладки">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar'
}
</script>

<style scoped>
.search-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 10;
}

.bottom-panel {
  position: absolute;
  width: 100%;
  height: 122px;
  background: #232323;
  border-radius: 30px 30px 0px 0px;
  bottom: 0;
}

.arrow-indicator {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 92px;
}

.arrow-indicator img {
  width: 29px;
  height: 29px;
}

.search-bar {
  position: absolute;
  bottom: 50px;
  left: 15px;
  right: 18px;
  display: flex;
  gap: 10px;
  align-items: center;
}

.search-input {
  flex: 1;
  position: relative;
  background: #121212;
  border: 1px solid #606060;
  border-radius: 10px;
  height: 41px;
  display: flex;
  align-items: center;
  padding: 0 10px;
}

.search-logo {
  width: 32px;
  height: 28px;
  margin-right: 10px;
}

.search-field {
  flex: 1;
  background: transparent;
  border: none;
  color: #FFFFFF;
  font-family: 'Inter', sans-serif;
  font-style: italic;
  font-weight: 700;
  font-size: 14px;
  opacity: 0.7;
}

.search-field::placeholder {
  color: #FFFFFF;
  opacity: 0.7;
}

.search-field:focus {
  outline: none;
}

.search-icon {
  width: 16px;
  height: 16px;
}

.bookmark-button {
  width: 41px;
  height: 41px;
  background: #111111;
  opacity: 0.9;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bookmark-button img {
  width: 37px;
  height: 37px;
}
</style>