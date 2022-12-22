<template>
    <div>
        <p>Hi from Wanted Shelf</p>
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