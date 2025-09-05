<template>
    <div id="yandex-map" ref="mapContainer" style="width: 375px; height: 445px;"></div>
</template>

<script>
export default {
    name: 'YandexMap',
    props: {
        center: {
            type: Array,
            default: () => [59.938784, 30.314997]
        },
        zoom: {
            type: Number,
            default: 10
        }
    },
    data() {
        return {
            map: null,
            ymaps: null
        }
    },
    mounted() {
        this.loadYandexMaps();
    },
    beforeUnmount() {
        this.destroyMap();
    },
    methods: {
        loadYandexMaps() {
            if (window.ymaps) {
                this.initMap();
                return;
            }

            const script = document.createElement('script');
            script.src = `https://api-maps.yandex.ru/2.1/?apikey=a89c2245-cce0-46dc-9120-bbfff9a1c06a&lang=ru_RU`;
            script.onload = () => {
                window.ymaps.ready(this.initMap);
            };
            document.head.appendChild(script);
        },

        initMap() {
            this.ymaps = window.ymaps;
            
            this.map = new this.ymaps.Map(this.$refs.mapContainer, {
                center: this.center,
                zoom: this.zoom
            });

            this.$emit('map-initialized', this.map, this.ymaps);
        },

        destroyMap() {
            if (this.map) {
                this.map.destroy();
                this.map = null;
            }
        }
    },
    watch: {
        center(newCenter) {
            if (this.map) {
                this.map.setCenter(newCenter);
            }
        },
        zoom(newZoom) {
            if (this.map) {
                this.map.setZoom(newZoom);
            }
        }
    }
}
</script>

<style scoped>
#yandex-map {
    border: 1px solid #ccc;
    border-radius: 8px;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>