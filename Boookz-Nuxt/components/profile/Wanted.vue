<template>
    <div class="w-full md:w-1/3">
  <h2 class="font-bold text-xl font-sans m-2">My Wanted Books</h2>

        <div v-for="book in store.userWantedBooks">
        <NuxtLink @click="store.setClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
            <BookCard :book="book" />
        </NuxtLink>
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