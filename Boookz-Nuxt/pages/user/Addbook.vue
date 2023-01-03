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
        id="book-images"
        type="file"
        multiple
        accept="image/*"
        @change="updateFiles($event.target.files)"
        class="border-2 border-black p-2 rounded-md"
      />

      <button type="submit" class="btn-sm self-center">submit</button>
    </form>

    <p>auth: {{ bookForm.author }}</p>
    <p>title: {{ bookForm.title }}</p>
    <p>image: {{ bookForm.images }}</p>
    <p>categ: {{ bookForm.category }}</p>
    <p>cond: {{ bookForm.condition }}</p>
    <p>lang: {{ bookForm.language }}</p>
  </div>
</template>

<script>
import { useUserStore } from "~/stores/userStore";
import { useLangAPIStore } from "~/stores/languagesStore";

export default {
  setup() {
    const userStore = useUserStore();
    const langStore = useLangAPIStore();
    const Languages = langStore.getAllLanguages();

    const conditions = ["poor", "fair", "good", "excellent"];
    const categories = ["fiction", "romance", "science"];

    // const route = useRoute();
    // const shelf = route;
    // console.log("shelf:", route.params.id);
    // const images = [];
    // const file = ref(null);

    const chosenLanguage = ref("");

    const images = null;

    const bookForm = reactive({
      title: "",
      author: [],
      category: "",
      condition: "",
      language: "",
      image: null,
    });

    function getLangCode() {
      console.log(chosenLanguage.value);
      bookForm.language = langStore.getLanguageCode(chosenLanguage.value);
    }

    function updateFiles(files) {
      this.images = files[0];
      bookForm.image = this.images;

      // const formData = new formData();
      // if (!files.length) return;
      // for (let i = 0; i < files.length; i++) {
      //   let file = files[i];
      //   formData.append("files[" + i + "]", file);
      // }
    }

    async function addBook() {
      userStore.addBook(bookForm);
    }

    return {
      chosenLanguage,
      conditions,
      categories,
      Languages,
      bookForm,
      updateFiles,
      getLangCode,
      addBook,
    };
  },

  methods: {},
};
</script>

<style scoped></style>
