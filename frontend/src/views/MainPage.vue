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
import Header from "@/components/Main_page/Header.vue"
import MapControls from "@/components/Main_page/MapControls.vue"
import SearchBar from "@/components/Main_page/SearchBar.vue"
import TransportFilters from "@/components/Main_page/TransportFilters.vue"
import Map from "@/components/Main_page/Map.vue"

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
