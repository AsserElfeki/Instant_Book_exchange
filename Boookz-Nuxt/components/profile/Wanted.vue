<template>
    <div class="w-full md:w-1/3">
        <div v-for="book in store.userWantedBooks">
            <BookCard :book="book" />
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '~/stores/userStore';
const store = useUserStore();
store.getUserWantedBooks();

</script>

<style scoped>

</style>