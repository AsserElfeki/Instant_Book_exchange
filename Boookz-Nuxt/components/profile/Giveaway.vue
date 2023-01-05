<template>
  <div class="flex flex-col mx-auto">
    <div v-if="!route.id" class="flex justify-center items-center my-8">
      <NuxtLink to="/user/addbook" class="btn"> add more </NuxtLink>
    </div>

    <div v-if="store.userGiveAwayBooks.length" 
    class="flex flex-col items-center justify-center w-full mx-auto px-4">
      <h2 v-if="route.id" class="font-bold text-xl font-sans m-2 self-start">{{store.userName}}'s Giveaway Books</h2>
      <h2 v-if="!route.id" class="font-bold text-xl font-sans m-2 self-start">My Giveaway Books</h2>
      <div class="flex gap-2 items-stretch">
          <NuxtLink 
            class="flex-1"
            v-for="book in store.userGiveAwayBooks"
            @click.left="dataStore.setClickedBook(book)"
            @click.middle="dataStore.setClickedBook(book)"
            @click.right="dataStore.setClickedBook(book)"
            :to="`/books/${book.title.replaceAll(' ', '-')}`"
          >
            <ProfileBookCard :book="book" />
          </NuxtLink>
      </div>
    </div>

    <div v-else class="mt-16">
      <LazyProfilePlaceHolder />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
import { useProfileStore } from "~/stores/profileStore";
import { useDataStore } from "~/stores/dataStore";
const route = useRoute().params;
const store = !route.id ? useUserStore() : useProfileStore();
const dataStore = useDataStore();
// await store.getUserInfo();
</script>

<style scoped></style>
