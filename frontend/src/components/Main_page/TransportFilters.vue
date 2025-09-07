<template>
  <div class="transport-filters">
    <div 
      v-for="filter in filters" 
      :key="filter.id" 
      class="filter-item"
      :class="{ active: filter.active }"
      @click="toggleFilter(filter.id)"
    >
      <div class="filter-bg"></div>
      <img :src="filter.icon" :alt="filter.name" class="filter-icon">
      <span class="filter-name" v-if="filter.name">{{ filter.name }}</span>
    </div>
  </div>
</template>

<script>
  // Импортируем изображения в начале компонента
  import allFiltersIcon from '@/assets/images/icontrans.png';
  import autoIcon from '@/assets/images/auto.png';
  import busIcon from '@/assets/images/bus.png';
  import metroIcon from '@/assets/images/metro.png';
  import trainIcon from '@/assets/images/train.png';
  import shipIcon from '@/assets/images/ship.png';
  import planeIcon from '@/assets/images/plane.png';

  export default {
    name: 'TransportFilters',
    data() {
      return {
        filters: [
          { id: 'all', name: 'Все', icon: allFiltersIcon, active: true },
          { id: 'auto', name: '', icon: autoIcon, active: false },
          { id: 'bus', name: '', icon: busIcon, active: false },
          { id: 'metro', name: '', icon: metroIcon, active: false },
          { id: 'train', name: '', icon: trainIcon, active: false },
          { id: 'ship', name: '', icon: shipIcon, active: false },
          { id: 'plane', name: '', icon: planeIcon, active: false }
        ]
      }
    },
    methods: {
      toggleFilter(filterId) {
        this.filters.forEach(filter => {
          if (filter.id === filterId) {
            filter.active = true;
          } else if (filterId === 'all') {
            // При выборе "Все" деактивируем остальные
            filter.active = filter.id === 'all';
          } else {
            // При выборе конкретного транспорта деактивируем "Все"
            if (filter.id === 'all') filter.active = false;
          }
        });
      }
    }
  }
</script>

  <style scoped>
  .transport-filters {
    position: fixed;
    bottom: 12px;
    left: 23px;
    display: flex;
    gap: 8px;
    z-index: 10;
  }

  .filter-item {
    position: relative;
    cursor: pointer;
  }

  .filter-bg {
    width: 28.68px;
    height: 28.68px;
    background: #DF793B;
    border-radius: 18px;
    transition: background-color 0.3s ease;
  }

  .filter-item.active .filter-bg {
    background: #F05E39;
  }

  .filter-item:first-child .filter-bg {
    width: 66.09px;
    height: 28.06px;
    border-radius: 14px;
  }

  .filter-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 22px;
    height: 22px;
    z-index: 1;
  }

  .filter-item:first-child .filter-icon {
    width: 28px;
    height: 28px;
    left: 14px;
  }

  .filter-name {
    position: absolute;
    top: 50%;
    left: 38px;
    transform: translateY(-50%);
    font-family: 'Inter', sans-serif;
    font-style: italic;
    font-weight: 700;
    font-size: 14px;
    color: #FFFFFF;
    opacity: 0.7;
    white-space: nowrap;
  }
</style>