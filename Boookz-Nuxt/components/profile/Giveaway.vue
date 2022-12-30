<template>
    <div class="w-full md:w-1/3  ">
        <div v-for="book in store.userGiveAwayBooks">
            <NuxtLink @click="store.setClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
                <BookCard :book="book" />
            </NuxtLink>
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