<template>
  <div class="container">

    <div class="">
      <RandomBook :book="store.randomBook" />
    </div>
    <div class="allgiveaways">
      <h2 class="flex justify-center text-3xl m-8 text-primary">Offered by our users in your area</h2>
      <div class="showcase">
        <div class="book" v-for="book in store.giveAwayBooks" :key="book.title">
          <NuxtLink v-on:click = "store.getClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
            <BookCard :book="book" />
          </NuxtLink>

        </div>

      </div>
    </div>
    <div class="allwanted">
      <h2 class="flex justify-center text-3xl m-8">Wanted by users in your area</h2>
      <div class="showcase">
        <div class="book" v-for="book in store.wantedBooks" :key="book.title">
          <NuxtLink v-on:click = "store.getClickedBook(book)" :to="`/books/${book.title.replaceAll(' ', '-')}`">
            <BookCard :book="book" />
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useDataStore } from '~/stores/dataStore'

const store = useDataStore()
</script>

<style scoped>
.hero {
  overflow: hidden;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  /* border: 3px solid blue; */
}

.showcase {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
  grid-gap: 1rem;
  margin: 1rem;
  /* border: 3px solid red; */
}
</style>

