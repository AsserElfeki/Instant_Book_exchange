<template>
  <div class="flex flex-col justify-center mb-4">
    <div
      v-if="store.randomBook"
      class="self-center w-full"
    >
      <RandomBook :book="store.randomBook" />
    </div>
    <div class="flex flex-col justify-center items-center">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Offered by users in your area
      </h2>
      <div
        v-if="store.giveAwayBooks.length > 0"
        class="flex flex-row flex-wrap gap-3 justify-center pb-6"
      >
        <BookCard
          v-for="book in store.giveAwayBooks"
          :key="book.pk"
          :book="book"
          class="w-1/3 md:w-1/4 my-4"
        />
      </div>
      <div
        v-else
        class="flex flex-col gap-2 items-center justify-center"
      >
        <font-awesome-icon
          icon="fa-solid fa-face-sad-tear"
          class="text-red-400 fa-xl"
        />
        <p class="text-lg">
          Oops, It seems no books are currently offered in your area.
        </p>
      </div>
    </div>

    <div class="flex flex-col justify-center items-center">
      <h2 class="flex justify-center text-3xl m-8 text-violet-600">
        Wanted by users in your area
      </h2>
      <div
        v-if="store.wantedBooks.length > 0"
        class="flex flex-row flex-wrap gap-3 justify-center pb-6"
      >
        <BookCard
          v-for="book in store.wantedBooks"
          :key="book.pk"
          :book="book"
          class="w-1/3 md:w-1/4 my-4"
        />
      </div>
      <div
        v-else
        class="flex flex-col gap-2 items-center justify-center"
      >
        <font-awesome-icon
          icon="fa-solid fa-face-sad-tear"
          class="text-red-400 fa-xl"
        />
        <p class="text-lg">
          Oops, It seems no books are currently wanted in your area.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useDataStore } from '~/stores/dataStore';

  const store = useDataStore();
</script>

<style scoped></style>
