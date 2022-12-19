<template>
  <div class="container">

    <div class="border border-solid border-red-500 border-3">
      <HeroBg />
      <RandomBook :book="store.randomBook" />
    </div>
    <div class="allgiveaways">
      <h2 class="flex justify-center text-3xl m-8 text-primary">Offered by our users in your area</h2>
      <div class="showcase">
        <div class="book" v-for="book in store.books" :key="book.title">
          <BookCard :book="book" />
        </div>

      </div>
    </div>
    <div class="allwanted">
      <h2 class="flex justify-center text-3xl m-8">Wanted by users in your area</h2>
      <div class="showcase">
        <div class="book" v-for="book in store.books" :key="book.title">
          <BookCard :book="book" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from '~/stores/store'

const store = useStore()
const { data: randomBook } = store.randomBook
</script>

<style scoped>
.hero {
  overflow: hidden;
  margin: 0;
  /* border: 3px solid blue; */
}
</style>


//ToDO: 
// 1. get data from store.js (loggedIn, books[]) ✅
// 2. process the data and render 
