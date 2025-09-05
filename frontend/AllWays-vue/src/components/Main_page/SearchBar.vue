<template>
  <div 
    class="search-container" 
    :class="{ expanded: isExpanded }"
    @touchstart="onTouchStart"
    @touchmove="onTouchMove"
    @touchend="onTouchEnd"
  >
    <div class="bottom-panel"></div>
    <div class="arrow-indicator" @click="toggleExpand">
      <img src="@/assets/images/arrow.png" alt="Индикатор" :class="{ rotated: isExpanded }">
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

    <!-- Дополнительный контент для развернутого состояния -->
    <div class="expanded-content" v-if="isExpanded">
      <div class="recent-searches">
        <h3>Недавние поиски</h3>
        <!-- Список недавних поисков -->
      </div>
      <div class="favorites">
        <h3>Избранное</h3>
        <!-- Список избранного -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      isExpanded: false,
      startY: 0,
      currentY: 0,
      isDragging: false
    }
  },
  methods: {
    onTouchStart(event) {
      this.startY = event.touches[0].clientY;
      this.isDragging = true;
    },
    
    onTouchMove(event) {
      if (!this.isDragging) return;
      
      this.currentY = event.touches[0].clientY;
      const deltaY = this.startY - this.currentY;
      
      // Если тянем вверх - расширяем
      if (deltaY > 50 && !this.isExpanded) {
        this.isExpanded = true;
        this.isDragging = false;
      }
      // Если тянем вниз - сворачиваем
      else if (deltaY < -50 && this.isExpanded) {
        this.isExpanded = false;
        this.isDragging = false;
      }
    },
    
    onTouchEnd() {
      this.isDragging = false;
    },
    
    toggleExpand() {
      this.isExpanded = !this.isExpanded;
    }
  }
}
</script>

<style scoped>
.search-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 10;
  transition: transform 0.3s ease;
}

.search-container.expanded {
  transform: translateY(calc(-100vh + 122px));
  height: 100vh;
}

.bottom-panel {
  position: absolute;
  width: 100%;
  height: 122px;
  background: #232323;
  border-radius: 30px 30px 0px 0px;
  bottom: 0;
  transition: height 0.3s ease;
}

.search-container.expanded .bottom-panel {
  height: 100%;
  border-radius: 0;
}

.arrow-indicator {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 92px;
  z-index: 11;
  cursor: pointer;
}

.arrow-indicator img {
  width: 29px;
  height: 29px;
  transition: transform 0.3s ease;
}

.arrow-indicator img.rotated {
  transform: rotate(180deg);
}

.search-bar {
  position: absolute;
  bottom: 50px;
  left: 15px;
  right: 18px;
  display: flex;
  gap: 10px;
  align-items: center;
  z-index: 12;
}

.expanded-content {
  position: absolute;
  top: 70px;
  left: 0;
  right: 0;
  padding: 20px;
  color: white;
  z-index: 11;
}

.recent-searches, .favorites {
  margin-bottom: 20px;
}

.recent-searches h3, .favorites h3 {
  margin-bottom: 10px;
  opacity: 0.8;
}

/* Для плавной анимации */
.search-container {
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
</style>