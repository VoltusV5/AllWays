<template>
    <div class="v-collapsible">
            <img @click="goToMainPage" class="v-collapsible_btn" src="@/assets/images/minus 2.png" alt="Arrow Back">
    </div>
</template>

<script>
export default {
    name: 'collapsible',
    methods: {
        goToMainPage() {
            try {
                this.$router.push('/');
            } catch (error) {
                console.error('Navigation error:', error);
            }
        }
    }
}
</script>

<style scoped>

.v-collapsible {
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
}

.v-collapsible_btn {
    background: none;
}

</style>

