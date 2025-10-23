<template>
    <div class="main_container">
        <collapsible /> 
        <h1>Маршрут</h1>

        <div class="route_build_menu">
            <!-- Используем компонент для "Откуда" -->
            <RouteInput     
                label="Откуда" 
                placeholder="введите начальную точку маршрута" 
                v-model="from" 
                />

            <!-- Кнопка для обмена местами -->
            <div class="swap_container">
                <button class="swap_btn">
                    <img src="@/assets/images/swap 1.png" />
                </button>
            </div>

            <!-- Используем компонент для "Куда" -->
            <RouteInput class="last_of_input"
                label="Куда" 
                placeholder="введите конечную точку маршрута" 
                v-model="to" 
                />

            <TransportFilters class="custom-transport-filters" />
        </div>

        
        <button class="find_route_btn" @click="findRoute" >Найти Маршруты</button>
        
        <div v-if="error" class="error-message">{{ error }}</div>
        <div v-if="routes.length" class="routes-list">
            <div v-for="route in routes" :key="route.id" class="route">
                <h4>{{ route.start }} - {{ route.end }}</h4>
                <p>{{ route.message }}</p>
            </div>
        </div>

        <div class="history">
            <h3>История</h3> 
            <div class="history_container">
                <div class="history_element"> 
                    <h4>Центральный парк</h4> 
                    <img src="@/assets/images/arrow_to_from.png" /> 
                    <h4>Центральный парк</h4> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                    <p>2 км</p> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                </div>
                <div class="history_element"> 
                    <h4>Центральный парк</h4> 
                    <img src="@/assets/images/arrow_to_from.png" /> 
                    <h4>Центральный парк</h4> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                    <p>2 км</p> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                </div>
                <div class="history_element"> 
                    <h4>Центральный парк</h4> 
                    <img src="@/assets/images/arrow_to_from.png" /> 
                    <h4>Центральный парк</h4> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                    <p>2 км</p> 
                    <h6>Москва, ул. Лесная, 15</h6> 
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import RouteInput from "@/components/RouteBuilder/RouteInput.vue";
import TransportFilters from "@/ui/TransportFilters.vue";
import collapsible from "@/ui/v-collapsible.vue";
import axios from 'axios';

export default {
    name: "RouteBuilder",
    components: {
        RouteInput,
        TransportFilters,
        collapsible
    },
    data() {
        return {
        from: "",
        to: "",
        routes: [],
        error: "",
        };
    },
    methods: {
        async findRoute() {
            if (!this.from || !this.to) {
                this.error = "Пожалуйста, укажите начальную и конечную точку маршрута!";
                return;
            }

            this.error = ""; // Сбрасываем предыдущие ошибки
            try {
                // Отправляем запрос на сервер с любым текстом
                const response = await axios.post('/api/routes/', {
                    from: this.from,
                    to: this.to,
                });

                if (response.data.routes) {
                    this.routes = response.data.routes;  // Получаем маршруты
                } else {
                    this.error = "Маршруты не найдены!";
                }
            } catch (err) {
                console.error("Ошибка при получении маршрутов:", err);
                this.error = "Ошибка связи с сервером. Попробуйте позже.";
            }
        }
    }
}
</script>

<style scoped>
.route_build_menu {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}

h1 { 
    font-size: 60px; 
    color: #fff; 
    text-align: center; 
    margin-bottom: 20px;
}



.swap_btn { 
    width: 50px; 
    height: 50px; 
    border-radius: 48px; 
    align-self: flex-start; 
}

.swap_container {
    display: flex;
    justify-content: flex-end;
    width: 90%;
    margin-bottom: 15px;
}

.last_of_input {
    margin-top: -33px;
    margin-bottom: 5px;
}

.custom-transport-filters {
    bottom: unset;
    position: relative;
    
}

.find_route_btn {
    background: #606060;
    color: #fff;
    opacity: 60%;
    border-radius: 20px;
    width: 90%;
    min-height: 60px;
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 30px;
}

.main_container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}



/* History */

.history {
    width: 100%;
}

h3 {
    color: #fff;
    font-size: 20px;
    padding-left: 20px;
}

.history_element:first-child {
    border-radius: 10px 10px 0px 0px;
}

.history_element {
    display: grid;
    justify-content: center;
    justify-items: center;   /* Центрируем по горизонтали */
    align-items: center; 
    grid-template-columns: 150px 50px 150px;
    grid-template-rows: 40px 20px;
    margin: 20px;
    margin-bottom: 10px;
    margin-top: 10px;
    background-color: #333333;
}

.history_element h4 {
    font-size: 13px;
    font-weight: bold;
    color: #fff;
    opacity: 80%;
}

.history_element h6 {
    font-size: 11px;
    color: #fff;
    opacity: 60%;
}
.history_element p {
    font-size: 10px;
    color: #B8A690;
}




</style>
