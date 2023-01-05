<template>
  <div
    class="bg-[#dddaee] max-w-xs shadow-xl relative rounded-3xl flex flex-col items-center overflow-visible p-3 h-80"
  >
    <NuxtLink
      @click.left="dataStore.setClickedBook(book)"
      @click.middle="dataStore.setClickedBook(book)"
      @click.right="dataStore.setClickedBook(book)"
      :key="book.pk"
      :to="`/books/${book.title.replaceAll(' ', '-')}`"
    >
      <div class="rounded-3xl w-full max-h-[800px] flex flex-col items-center">
        <img
          :src="book.images.at(0)"
          :alt="book.title"
          class="rounded-3xl max-h-44 object-contain"
        />

        <h4 class="text-[#e76f51] text-center text-sm md:text-xl md:leading-tight">
          {{ truncate(book.title, 28) }}
        </h4>
      </div>
    </NuxtLink>

    <div class="flex flex-col justify-end min-w-full pb-4 h-full">
      <p class="text-sm md:text-lg mb-1">by: {{ book.book_owner.username }}</p>
    </div>
    <NuxtLink
      class="flex flex-col justify-end pb-4"
      :to="`/profile/${book.book_owner.username.replaceAll(' ', '-')}`"
    >
      <img
        v-if="book.book_owner.profile_image"
        :src="book.book_owner.profile_image"
        :alt="book.book_owner.username"
        class="user-image w-16 h-16 rounded-full object-cover absolute bottom-[-40px] left-1/2 -translate-x-1/2 border-black border"
      />
    </NuxtLink>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
import { useDataStore } from "~/stores/dataStore";
const { book } = defineProps(["book"]);
const store = useUserStore();
const dataStore = useDataStore();
function truncate(string, value) {
  if (string.length > value) return string.substring(0, value) + "…";
  else return string;
}
</script>

<style scoped></style>
