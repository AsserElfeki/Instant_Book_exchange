<template>
  <div class="flex flex-col justify-center">
    <div class=" self-center">
      <RandomBook :book="store.randomBook" />
    </div>
    <div class="allgiveaways">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Offered by users in your area
      </h2>
      <div class="showcase">
        <div class="mx-auto w-2/3 md:w-full" v-for="book in store.giveAwayBooks" :key="book.pk">
          <NuxtLink v-on:click="store.setClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
            <BookCard :book="book" />
          </NuxtLink>
        </div>
      </div>
    </div>
    <div class="allwanted">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600 ">Wanted by users in your area</h2>
      <div class="showcase">
        <div class="mx-auto w-2/3 md:w-full" v-for="book in store.wantedBooks" :key="book.title">
          <NuxtLink @click="store.setClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
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

onBeforeRouteLeave(to, from, next) {
    this.doSomething();
    next();
}
  
</script>

<style scoped>
.showcase {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 1rem;
  /* margin: 1rem;  */
  /* border: 3px solid red; */
}
</style>
