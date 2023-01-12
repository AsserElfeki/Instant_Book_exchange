<template>
  <div class="flex flex-col justify-center mb-4">
    <div
      v-if="dataStore.randomBook"
      class="self-center w-full"
    >
      <RandomBook :book="dataStore.randomBook" />
    </div>

    <div class="flex flex-col justify-center items-center">
      <h2
        v-if="userStore.userIsLoggedIn"
        class="flex justify-center text-4xl m-8 text-violet-600"
      >
        Offered books by users in your area
      </h2>
      <h2
        v-else
        class="flex justify-center text-4xl m-8 text-violet-600"
      >
        Offered books
      </h2>

      <div class="flex flex-col gap-4">
        <div
          v-if="dataStore.giveAwayBooks.length > 0"
          class="flex flex-row flex-wrap gap-3 justify-center pb-4"
        >
          <BookCard
            v-for="book in loadedGiveawayBooks"
            :key="book.pk"
            :book="book"
            class="w-1/3 md:w-1/4 my-6"
          />
        </div>

        <div
          v-show="!dataStore.giveAwayBooks.length"
          class="flex flex-col gap-2 items-center justify-center"
        >
          <p class="text-lg">
            Oops, It seems no books are currently offered in your area.
          </p>
          <font-awesome-icon
            icon="fa-solid fa-face-sad-tear"
            class="text-red-400 fa-xl"
          />
        </div>

        <div
          v-if="dataStore.giveAwayBooks.length >= giveawayBooksEnd"
          class="btn-sm self-center"
        >
          <button @click="showMoreGiveawayBooks">show more</button>
        </div>
      </div>
    </div>

    <hr class="separator mx-auto" />

    <div class="flex flex-col justify-center items-center">
      <h2
        v-if="userStore.userIsLoggedIn"
        class="flex justify-center text-4xl m-8 text-violet-600"
      >
        Wanted books by users in your area
      </h2>
      <h2
        v-else
        class="flex justify-center text-4xl m-8 text-violet-600"
      >
        Wanted books
      </h2>
      <div class="flex flex-col gap-2">
        <div
          v-if="dataStore.wantedBooks.length > 0"
          class="flex flex-row flex-wrap gap-3 justify-center pb-6"
        >
          <BookCard
            v-for="book in loadedWantedBooks"
            :key="book.pk"
            :book="book"
            class="w-1/3 md:w-1/4 my-6"
          />
        </div>
        <div
          v-show="!dataStore.wantedBooks.length"
          class="flex flex-col gap-2 items-center justify-center"
        >
          <p class="text-lg">
            Oops, It seems no books are currently wanted in your area.
          </p>
          <font-awesome-icon
            icon="fa-solid fa-face-sad-tear"
            class="text-red-400 fa-xl"
          />
        </div>
        <div
          v-if="dataStore.wantedBooks.length >= wantedBooksEnd"
          class="btn-sm self-center"
        >
          <button @click="showMoreWantedBooks">show more</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useDataStore } from '~/stores/dataStore';
  import { useUserStore } from '~/stores/userStore';
  const dataStore = useDataStore();
  const userStore = useUserStore();

  await dataStore.getWantedBooksFromDB();
  await dataStore.getOfferedBooksFromDB();

  const start = 0;
  const wantedBooksEnd = ref(6);
  const giveawayBooksEnd = ref(6);

  const loadedGiveawayBooks = computed(() => {
    if (dataStore.giveAwayBooks.length >= giveawayBooksEnd.value)
      return dataStore.giveAwayBooks.slice(start, giveawayBooksEnd.value);
    else {
      return dataStore.giveAwayBooks;
    }
  });

  const loadedWantedBooks = computed(() => {
    if (dataStore.wantedBooks.length >= wantedBooksEnd.value)
      return dataStore.wantedBooks.slice(start, wantedBooksEnd.value);
    else {
      return dataStore.wantedBooks;
    }
  });

  function showMoreGiveawayBooks() {
    giveawayBooksEnd.value += 6;
  }

  function showMoreWantedBooks() {
    wantedBooksEnd.value += 6;
  }
</script>

<style scoped></style>
