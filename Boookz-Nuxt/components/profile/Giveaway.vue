<template>
    <div>
        <p>Hi from GiveAway Shelf</p>
        <div v-for="book in store.userGiveAwayBooks">
            <BookCard :book="book"> </BookCard>
        </div>

    </div>
</template>

<script setup>
import { useUserStore } from '~/stores/userStore';
const store = useUserStore();
store.getUserGiveAwayBooks();


</script>

<style scoped>

</style>