<template>
    <div>
        <Header />
        <MapControls />
        <Map />
        <SearchBar />
        <TransportFilters />
    </div>
</template>

<script>
import Header from "@/components/MainPage/Header.vue"
import MapControls from "@/components/MainPage/MapControls.vue"
import SearchBar from "@/components/MainPage/SearchBar.vue"
import TransportFilters from "@/components/MainPage/TransportFilters.vue"
import Map from "@/components/MainPage/Map.vue"

export default {
    name: "MainPage",
    components: {
    Header,
    MapControls,
    SearchBar,
    TransportFilters,
    Map
}
}
</script>