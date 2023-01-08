<template>
  <div class="flex flex-wrap justify-center gap-10 px-4 py-10">
    <div 
    v-if="dataStore.searchResults.length"
    v-for="book in dataStore.searchResults"
    class="flex-auto flex justify-center basis-1/4 max-h-min"
    >
      <BookCard :book="book" class="w-full "/>
    </div>
    <div
    v-else 
    class="flex gap-2 items-center">
    <font-awesome-icon icon="fa-solid fa-face-sad-tear" class="text-red-400 fa-xl"/>
    <p class="text-lg">Sorry, no books found matching your search</p>
    </div>
  </div>
</template>

<script setup>
import { useDataStore } from '~/stores/dataStore';
const dataStore = useDataStore();
</script>

<style  scoped>

</style>