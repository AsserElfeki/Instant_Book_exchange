<template>
  <div class="container">

    <div class="hero ">
      <HeroBg></HeroBg>
      <RandomBook book="`${booksData.books[1]}`" />
    </div>
    <div class="allgiveaways">
      <h2 class="flex justify-center text-2xl text-primary">Offered by our users in your area</h2>
      <div class="showcase">
        <div class="book" v-for="book in booksData.books" :key="book.title">
          <BookCard :book="book" />
        </div>

      </div>
    </div>
    <div class="allwanted">
      <h2 class="flex justify-center text-2xl text-primary">Wanted by users in your area</h2>
      <div class="book-info">

      </div>
      <div class="showcase">
        <!-- books -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from '~/stores/store'

const booksData = useStore()

// const { data: booksData } = await useFetch('http://localhost:4000/books')
// const books = store.books
// const book = books

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
