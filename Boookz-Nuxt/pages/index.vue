<template>
  <div class="flex flex-col justify-center">
    <div class="self-center w-full">
      <RandomBook :book="store.randomBook" />
    </div>
    <div
      class="allgiveaways flex flex-col justify-center items-center"
    >
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Offered by users in your area
      </h2>
      <div class="flex flex-row flex-wrap gap-3 justify-center items-center">
        <div class="w-1/2 my-2 md:w-1/4" v-for="book in store.giveAwayBooks" :key="book.pk">
          <NuxtLink
            v-on:click="store.setClickedBook(book)"
            :to="`/books/${book.title.replaceAll(' ', '-')}`"
          >
            <BookCard :book="book" />
          </NuxtLink>
        </div>
      </div>
    </div>
    <div class="allwanted flex flex-col justify-center items-center">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Wanted by users in your area
      </h2>
      <div class="flex flex-row flex-wrap gap-3 justify-center items-center">
        <div
          class="w-1/2 my-2 md:w-1/4"
          v-for="book in store.wantedBooks"
          :key="book.title"
        >
          <NuxtLink
            @click="store.setClickedBook(book)"
            :to="`/books/${book.title.replaceAll(' ', '-')}`"
          >
            <BookCard :book="book" />
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useDataStore } from "~/stores/dataStore";

const store = useDataStore();
</script>

<style scoped>

</style>
