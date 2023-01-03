<template>
  <div class="flex flex-col justify-center items-center border-2 border-red-500">
    <form
      @submit.prevent="addBook"
      enctype="multipart/form-data"
      class="flex flex-col justify-start gap-3 border-2 w-full md:w-1/2 items-start mx-auto p-2"
    >
      <div class="flex justify-between gap-6">
        <label for="language">Language:</label>
        <select
          id="language"
          v-model="chosenLanguage"
          @change="getLangCode"
          size="1"
          class="border-2 rounded-md overflow-y-scroll max-h-12 w-44 text-center"
        >
          <option value="" disabled>-Select Language-</option>

          <option v-for="language in Languages" :key="language" :value="language">
            {{ language }}
          </option>
        </select>
      </div>

      <label for="book-title" class="self-start">Book title:</label>
      <input
        required
        size="40"
        id="book-title"
        type="text"
        v-model="bookForm.title"
        placeholder="Book title"
        class="border-2 border-black p-2 rounded-md"
      />

      <label for="book-author" class="self-start">Authors:</label>
      <input
        required
        size="40"
        id="book-author"
        type="text"
        v-model="bookForm.author"
        placeholder="authors"
        class="border-2 border-black p-2 rounded-md"
      />

      <div class="flex justify-between gap-6">
        <label for="category">Category(s):</label>
        <select
          id="category"
          v-model="bookForm.category"
          size="1"
          class="overflow-y-scroll h-auto border-2 rounded-md w-44 text-center"
        >
          <option value="" disabled>-Select category-</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>

      <div class="flex justify-between gap-6">
        <label for="condition">Condition:</label>
        <select
          id="condition"
          v-model="bookForm.condition"
          size="1"
          class="overflow-y-scroll h-auto border-2 rounded-md w-44 text-center"
        >
          <option value="" disabled>-Select Condition-</option>
          <option v-for="condition in conditions" :key="condition" :value="condition">
            {{ condition }}
          </option>
        </select>
      </div>

      <label for="book-images" class="self-start">upload images:</label>
      <input
        required
        id="book-images"
        type="file"
        multiple
        accept="image/*"
        class="border-2 border-black p-2 rounded-md"
      />

      <button type="submit" class="btn-sm self-center">submit</button>
    </form>

    <p>{{ bookForm }}</p>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
import { useLangAPIStore } from "~/stores/languagesStore";
const store = useUserStore();
const langStore = useLangAPIStore();
const Languages = langStore.getAllLanguages();

const conditions = ["poor", "fair", "good", "excellent"];
const categories = ["fiction", "romance", "science"];

const images = [];
const file = ref(null);

const chosenLanguage = ref("");
function getLangCode() {
  console.log(chosenLanguage.value);
  bookForm.language = langStore.getLanguageCode(chosenLanguage.value);
}
const bookForm = reactive({
  // token: store.token,
  title: "",
  author: "",
  // image: "",
  condition: "",
  category: "",
  language: "",
});

async function addBook() {
  store.addBook(bookForm);
}
</script>

<style scoped></style>
