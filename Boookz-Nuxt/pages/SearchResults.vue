<template>
  <div class="flex flex-wrap justify-center gap-10 px-4 py-10">
    <div 
    v-for="book in dataStore.searchResults"
    class="flex-auto flex justify-center basis-1/4 max-h-min"
    >
      <BookCard :book="book" class="w-full "/>
    </div>
  </div>
</template>

<script setup>
import { useDataStore } from '~/stores/dataStore';
const dataStore = useDataStore();
</script>

<style  scoped>

</style>