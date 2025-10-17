<template>
    <div class="input_group">
        <p class="input_info">{{ label }}</p>
        <input 
            class="input_container" 
            :placeholder="placeholder" 
            :value="modelValue" 
            @input="updateValue"
        />
    </div>
</template>

<script>
export default {
    name: 'RouteInput',
    props: {
        label: String,
        placeholder: String,
        modelValue: String,
    },
    methods: {
        updateValue(event) {
        this.$emit('update:modelValue', event.target.value);
        }
    }
}
</script>

<style scoped>
.input_group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 90%;
}

.input_info {
    font-size: 16px;
    color: #fff;
    opacity: 60%;
}

.input_container {
    text-align: center;
    width: 100%;
    min-height: 40px;
    max-height: 80px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}
</style>
