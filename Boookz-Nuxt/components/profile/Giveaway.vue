<template>
    <div v-if="store.userGiveAwayBooks.length"
    class="w-full md:w-1/3  ">
  <h2 class="font-bold text-xl font-sans m-2">My Giveaway Books</h2>

        <div v-for="book in store.userGiveAwayBooks">
            <NuxtLink @click="store.setClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
                <BookCard :book="book" />
            </NuxtLink>
        </div>

    </div>

     <div v-else class="mt-16">
    <LazyProfilePlaceHolder />
  </div>
</template>

<script setup>
import { useUserStore } from '~/stores/userStore';
const store = useUserStore();
await store.getUserGiveAwayBooks();


</script>

<style scoped>

</style>