<template>
  <div class="flex flex-col mx-auto">
    <div
      v-if="!route.id"
      class="flex justify-center items-center my-8"
    >
      <NuxtLink
        to="/user/addbook"
        class="btn"
      >
        add more
      </NuxtLink>
    </div>

    <div
      v-if="store.userWantedBooks.length"
      class="flex flex-col items-center justify-center w-full mx-auto px-4"
    >
      <h2
        v-if="route.id"
        class="font-bold text-xl m-2 self-start"
      >
        {{ store.userName }}'s Wanted Books
      </h2>
      <h2
        v-else
        class="font-bold text-xl m-2 self-start"
      >
        My Wanted Books
      </h2>

      <div class="flex flex-wrap gap-2 justify-center w-full">
        <div
          v-for="book in store.userWantedBooks"
          :key="book.pk"
          class="mt-12 basis-1/3 sm:basis-1/4 flex flex-col justify-between gap-2"
        >
          <NuxtLink
            class="h-full"
            @click.left="dataStore.setClickedBook(book)"
            @click.middle="dataStore.setClickedBook(book)"
            @click.right="dataStore.setClickedBook(book)"
            :to="`/books/${book.title.replaceAll('/', '-')}`"
          >
            <ProfileBookCard :book="book" />
          </NuxtLink>
          <div v-if="!route.id" class="btn-sm self-center">
            <button
              @click="deleteBook(book)"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>

    <div
      v-else
      class="mt-16"
    >
      <LazyProfilePlaceHolder />
    </div>
  </div>
</template>

<script setup>
  import { useUserStore } from '~/stores/userStore';
  import { useProfileStore } from '~/stores/profileStore';
  import { useDataStore } from '~/stores/dataStore';
  const route = useRoute().params;
  const store = !route.id ? useUserStore() : useProfileStore();
  const dataStore = useDataStore();

  function deleteBook(book) {
    store.deleteBook(book);
  }
  // await store.getUserInfo();
</script>

<style scoped></style>
