<template>
    <div>
        <h1>Book {{ id }}</h1>
    </div>
</template>

<script setup>
const { id } = useRoute().params
definePageMeta({
        // layout: 'books'
    })
</script>

<style scoped>

</style>