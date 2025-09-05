<!-- HTML -->
<template>
  <div id="app">
    <Header />
    <MapControls />
    <Map />

    <!-- <div class="map-container">
      <img src="./assets/images/map.png" alt="Карта" class="map-image">
    </div> -->

    <SearchBar />
    <TransportFilters />
    <!-- <Slider v-if="false" /> -->
  </div>
</template>

<!-- JS -->
<script>
  import Header from "./components/Main_page/Header.vue"
  import MapControls from "./components/Main_page/MapControls.vue"
  import SearchBar from './components/Main_page/SearchBar.vue'
  import TransportFilters from './components/Main_page/TransportFilters.vue'
  // import Slider from './components/Main_page/Slider.vue';
  import Map from './components/Main_page/Map.vue';

  export default {
    name: 'App',
    components: {
      Header,
      MapControls,
      SearchBar,
      TransportFilters,
      // Slider,
      Map
    }
  }

</script>

<!-- CSS -->
<style scoped>
  .map-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
  }

  .map-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>