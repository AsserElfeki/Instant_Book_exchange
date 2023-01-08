<template>
  <div class="flex flex-col justify-center mb-4">
    <div class="self-center w-full">
      <RandomBook :book="store.randomBook" />
    </div>
    <div class="flex flex-col justify-center items-center ">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Offered by users in your area
      </h2>
      <div class="flex flex-row flex-wrap gap-3 justify-center pb-6 w-full">
            <BookCard 
            v-for="book in store.giveAwayBooks"
            :key="book.pk"
            :book="book" 
            class="w-1/3 md:w-1/4 my-4"
            />
      </div>
    </div>

    <div class="flex flex-col justify-center items-center">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Wanted by users in your area
      </h2>
      <div
        class="flex flex-row flex-wrap gap-3 justify-center pb-6 w-full">
            <BookCard 
            v-for="book in store.wantedBooks"
            :key="book.pk"
            :book="book" 
            class="w-1/3 md:w-1/4 my-4"
            />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useDataStore } from "~/stores/dataStore";

const store = useDataStore();
</script>

<style scoped></style>
