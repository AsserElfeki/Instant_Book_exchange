<template>
  <div>
    hello from adding a book
    <form
      @submit.prevent="register"
      @input="store.resetErrors"
      class="flex flex-col justify-between gap-3 border-2 w-full md:w-1/2 items-center mx-auto"
    >

    <label for="book-lang" class="self-start">Book language:</label>
      <input
        required
        size="40"
        name="book-lang"
        type="text"
        v-model="form.language"
        placeholder="Language"
        class="border-2 border-black p-2 rounded-md"
      />

      <label for="book-title" class="self-start">Book title:</label>
      <input
        required
        size="40"
        name="book-title"
        type="text"
        v-model="form.title"
        placeholder="Book title"
        class="border-2 border-black p-2 rounded-md"
      />

      <label for="book-author" class="self-start">Book title:</label>
      <input
        required
        size="40"
        name="book-author"
        type="text"
        v-model="form.author"
        placeholder="authors"
        class="border-2 border-black p-2 rounded-md"
      />
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const store = useUserStore();
const books = store.userGiveAwayBooks;

const form = reactive({
  title: "",
  author: "",
  description: "",
  image: "",
  condition: "",
  category: "",
  language: "",
});
</script>

<style scoped></style>
