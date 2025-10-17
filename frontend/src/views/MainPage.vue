<template>
    <div>
        <Header />
        <MapControls />
        <Map />
        <SearchBar @click="GoToRouteBuilder" />
        <TransportFilters />
    </div>
</template>

<script>
import Header from "@/components/MainPage/Header.vue"
import MapControls from "@/components/MainPage/MapControls.vue"
import SearchBar from "@/components/MainPage/SearchBar.vue"
import TransportFilters from "@/ui/TransportFilters.vue"
import Map from "@/components/MainPage/Map.vue"

export default {
    name: "MainPage",
    components: {
    Header,
    MapControls,
    SearchBar,
    TransportFilters,
    Map,
    },
    methods: {
            GoToRouteBuilder() {
                try {
                    this.$router.push('/build-route');
                } catch (error) {
                    console.error('Navigation error:', error);
                }
            }
        }
    
}
</script>