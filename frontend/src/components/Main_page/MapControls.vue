<template>
  <div class="map-controls"> 
    <!-- Кнопка расстояния -->
    <div class="control-group distance-control">
      <div class="rectangle control-bg"></div>
      <div class="distance control-icon">
        <img src="@/assets/images/distance.png" alt="Расстояние">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MapControls'
}
</script>

<style scoped>
  .map-controls {
    position: fixed;
    /* right: 10px;
    top: 45%; */
    /* transform: translateY(-50%); */
    z-index: 10;
  }

  .control-group {
    position: relative;
    margin-bottom: 10px;
  }

  .control-bg {
    background-color: #000000;
    width: 45px;
    height: 45px;
    opacity: 0.7;
    border-radius: 17px;
  }

  .control-icon {
    position: absolute;
    top: 0;
    left: 0;
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0.8;
  }

  .control-icon img {
    width: 100%;
    height: 100%;
  }

  .distance-control {
    position: absolute;
    left: 14px;
    top: 439px;
  }

  .distance-control .control-bg {
    background: #191F1F;
    opacity: 0.9;
  }

  .distance-control .control-icon {
    width: 32px;
    height: 32px;
    left: 7px;
    top: 6px;
  }
</style>