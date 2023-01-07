<template>
  <div>
    <div
      v-if="store.userGiveAwayBooks.length"
      class="flex flex-col items-center justify-center w-full mx-auto px-4"
    >
      <h1 class="font-bold font-serif md:text-3xl inline mr-3 ml-3 mb-6">
        Choose one of your giveaway books :))
      </h1>
      <div
        class="flex flex-row flex-wrap gap-3 justify-center items-stretch pb-6"
      >
        <div
          v-for="book in store.userGiveAwayBooks"
          class="w-1/3 md:w-1/4 my-4"
          :class="{ selected: book.selected }"
          @click="toggleSelect(book)"
        >
          <ProfileBookCard :book="book" />
        </div>
      </div>
      <button
        class="btn-sm w-28 m-4"
        @click="confirmChoice"
      >
        Confirm
      </button>
    </div>
    <div v-if="selectedBook">Selected book: {{ selectedBook.title }}</div>
  </div>
</template>

<script setup>
  import { useUserStore } from '~/stores/userStore';
  import { useDataStore } from '~/stores/dataStore';
  const store = useUserStore();
  const dataStore = useDataStore();
  const selectedBook = ref(null);
  const clickedBook = dataStore.clickedBook;

  // toggleSelect: book is the parameter
  function toggleSelect(book) {
    // toggleSelect: if book.selected is true
    if (book.selected) {
      // toggleSelect: set book.selected to false
      book.selected = false;
      // toggleSelect: set selectedBook.value to null
      selectedBook.value = null;
    } else {
      // toggleSelect: if book.selected is false, loop through the store.userGiveAwayBooks array
      store.userGiveAwayBooks.forEach((b) => {
        // toggleSelect: for each book, set book.selected to false
        b.selected = false;
      });
      // toggleSelect: after looping through the store.userGiveAwayBooks array, set book.selected to true
      book.selected = true;
      // toggleSelect: set selectedBook.value to book
      selectedBook.value = book;
    }
  }

  function confirmChoice() {
    store.startTransaction(selectedBook.value.pk, clickedBook.pk);
  }
</script>

<style scoped>
  .selected {
    border: 3px solid blue;
  }
</style>
