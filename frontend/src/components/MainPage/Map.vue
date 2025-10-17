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
            ymaps: null,
            isDestroyed: false
        }
    },
    mounted() {
        this.loadYandexMaps();
    },
    beforeUnmount() {
        this.isDestroyed = true;
        this.safeDestroyMap();
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
                if (this.isDestroyed) return;
                window.ymaps.ready(() => {
                    if (this.isDestroyed) return;
                    this.initMap();
                });
            };
            script.onerror = (error) => {
                console.error('Failed to load Yandex Maps:', error);
            };
            document.head.appendChild(script);
        },

        initMap() {
            try {
                this.ymaps = window.ymaps;
                
                if (!this.$refs.mapContainer || this.isDestroyed) return;
                
                this.map = new this.ymaps.Map(this.$refs.mapContainer, {
                    center: this.center,
                    zoom: this.zoom,
                    behaviors: ['default', 'scrollZoom'],
                    controls: []
                });

                this.$emit('map-initialized', this.map, this.ymaps);
            } catch (error) {
                console.error('Error initializing map:', error);
            }
        },

        safeDestroyMap() {
            try {
                if (!this.map) return;
                
                // Правильное удаление geoObjects
                if (this.map.geoObjects && typeof this.map.geoObjects.removeAll === 'function') {
                    this.map.geoObjects.removeAll();
                }
                
                // Правильное удаление элементов управления
                if (this.map.controls) {
                    // Получаем все элементы управления и удаляем их по одному
                    const controls = this.map.controls.getAll();
                    controls.forEach(control => {
                        try {
                            this.map.controls.remove(control);
                        } catch (e) {
                            // Игнорируем ошибки при удалении контролов
                        }
                    });
                }
                
                // Даем время на очистку перед разрушением
                setTimeout(() => {
                    try {
                        if (this.map && typeof this.map.destroy === 'function') {
                            // Самый безопасный способ - просто очищаем контейнер
                            this.map.container.destroy();
                        }
                    } catch (error) {
                        console.warn('Warning during map destruction:', error);
                        // В крайнем случае просто очищаем HTML
                        this.forceCleanup();
                    }
                    
                    this.map = null;
                    this.ymaps = null;
                }, 50);
                
            } catch (error) {
                console.warn('Error in safeDestroyMap:', error);
                this.forceCleanup();
            }
        },

        forceCleanup() {
            // Принудительная очистка без использования API Яндекс Карт
            try {
                if (this.$refs.mapContainer) {
                    this.$refs.mapContainer.innerHTML = '';
                }
            } catch (e) {
                console.warn('Force cleanup error:', e);
            }
            this.map = null;
            this.ymaps = null;
        }
    },
    watch: {
        center(newCenter) {
            if (this.map && !this.isDestroyed) {
                try {
                    this.map.setCenter(newCenter);
                } catch (error) {
                    console.warn('Error setting center:', error);
                }
            }
        },
        zoom(newZoom) {
            if (this.map && !this.isDestroyed) {
                try {
                    this.map.setZoom(newZoom);
                } catch (error) {
                    console.warn('Error setting zoom:', error);
                }
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