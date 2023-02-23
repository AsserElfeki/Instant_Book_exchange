<template>
  <div>
    <div
      v-if="books.length"
      class="flex flex-col items-center justify-center w-full mx-auto px-4"
    >
      <h1 class="font-bold font-serif md:text-3xl inline mr-3 ml-3 mb-6">
        {{ tradeMessage }}
      </h1>
      <div
        class="text-sm md:text-md flex flex-row flex-wrap justify-around gap-2 mb-5 w-full"
      >
        <div
          v-for="book in books"
          class="cursor-pointer basis-1/4"
          :class="{ selected: book.selected }"
          @click="toggleSelect(book)"
        >
          <ProfileBookCard
            :book="book"
            class="overflow-hidden"
          />
        </div>
      </div>
      <div class="btn">
        <button
          class=""
          @click="confirmChoice"
        >
          Confirm
        </button>
      </div>
    </div>
    <div v-if="selectedBook">Selected book: {{ selectedBook.title }}</div>
  </div>
</template>

<script setup>
  import { useUserStore } from '~/stores/userStore';
  import { useDataStore } from '~/stores/dataStore';
  import { useProfileStore } from '../stores/profileStore';

  const {$toast} = useNuxtApp();
  const userStore = useUserStore();
  const profileStore = useProfileStore();
  const dataStore = useDataStore();
  const selectedBook = ref(null);
  const clickedBook = dataStore.clickedBook;
  const books = ref([]);
  const clickedBookShelf = clickedBook.book_shelf;
  const tradeMessage = ref('');
  profileStore.userName = clickedBook.book_owner.username;
  if (clickedBookShelf === 'wanted') {
    await profileStore.getUserInfo();
    books.value = profileStore.userGiveAwayBooks;
    tradeMessage.value =
      'Choose one of the book given-away by ' + profileStore.userName + ' :))';
  } else {
    books.value = userStore.userGiveAwayBooks;
    tradeMessage.value = ':)) Choose one of yours given-away books';
  }

  // toggleSelect: book is the parameter
  function toggleSelect(book) {
    // toggleSelect: if book.selected is true
    if (book.selected) {
      // toggleSelect: set book.selected to false
      book.selected = false;
      // toggleSelect: set selectedBook.value to null
      selectedBook.value = null;
      // toggleSelect: if book.selected is false, loop through the store.userGiveAwayBooks array
    } else {
      if (clickedBookShelf === 'giveaway') {
        userStore.userGiveAwayBooks.forEach((b) => {
          b.selected = false;
        });
      } else {
        profileStore.userGiveAwayBooks.forEach((b) => {
          b.selected = false;
        });
      }
      book.selected = true;
      // toggleSelect: set selectedBook.value to book
      selectedBook.value = book;
    }
  }

  function confirmChoice() {
    if (clickedBookShelf === 'giveaway') {
      userStore.startTransaction(selectedBook.value.pk, clickedBook.pk);
    } else {
      userStore.startTransaction(
        userStore.chosenBookForATrade.pk,
        selectedBook.value.pk
      );
    }

    $toast.success('Transaction started');
  }
</script>

<style scoped>
  .selected {
    /*shadow right bottom */

    --tw-shadow: 10px 15px 15px 3px rgba(96, 28, 206, 0.532),
      0 4px 6px -2px rgba(0, 0, 0, 0.05);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    border-radius: 28px;
  }
</style>
