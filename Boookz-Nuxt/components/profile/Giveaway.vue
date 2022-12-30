<template>
    <div class="w-full md:w-1/3  ">
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