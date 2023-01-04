<template>
  <div class="flex flex-col justify-center items-center border-2 border-red-500">
    <form
      @submit.prevent="addBook"
      enctype="multipart/form-data"
      class="flex flex-col justify-start gap-3 border-2 w-full md:w-1/2 items-start mx-auto p-2"
    >
      <div class="flex justify-between gap-6">
        <label for="shelf">Shelf:</label>
        <select
          id="shelf"
          v-model="bookForm.shelf"
          class="border-2 rounded-md overflow-y-scroll max-h-12 w-44 text-center"
        >
          <option value="" disabled>-Select Shelf-</option>
          <option value="giveaway">Giveaway shelf</option>
          <option value="wanted">Wanted shelf</option>
        </select>
      </div>

      <div class="flex justify-between gap-6">
        <label for="language">Language:</label>
        <select
          id="language"
          v-model="chosenLanguage"
          @change="getLangfullName"
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
        v-model="author"
        placeholder="authors"
        class="border-2 border-black p-2 rounded-md"
      />

      <div class="flex justify-between gap-6">
        <label for="category">Category(s):</label>
        <select
          id="category"
          v-model="category"
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
        accept=".png, .jpg, .jpeg"
        @change="updateFiles($event.target.files)"
        class="border-2 border-red-500 p-2 rounded-md"
      />

      <button type="submit" class="btn-sm self-center">submit</button>
    </form>

    <p>author: {{ bookForm.author }}</p>
    <p>title: {{ bookForm.title }}</p>
    <p>image: {{ bookForm.image }}</p>
    <p>category: {{ bookForm.category }}</p>
    <p>condition: {{ bookForm.condition }}</p>
    <p>language: {{ bookForm.language }}</p>
    <p>description: {{ bookForm.description }}</p>
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

    const conditions = ["Bad", "Perfect", "Good"];
    const categories = ["fiction", "romance", "science"];

    // const route = useRoute();
    // const shelf = route;
    // console.log("shelf:", route.params.id);
    // const images = [];
    // const file = ref(null);

    const chosenLanguage = ref("");

    const images = ref(null);

    const author = ref("");
    const category = ref("");

    const fd = new FormData();

    const bookForm = reactive({
      title: "",
      author: [],
      category: [],
      condition: "",
      language: "",
      image: [],
      description: "asdasdsad",
      shelf: "",
    });

    function getLangfullName() {
      langStore.chooseLanguage(chosenLanguage.value);
      bookForm.language = langStore.chosenLangEnglishName;
    }

    function updateFiles(files) {
      // this.images = files[0];
      // bookForm.image.push(images);
      // fd.append("image", images)

      if (!files.length) return;
      for (let i = 0; i < files.length; i++) {
        let file = files[i];
        fd.append("image", file);
      }
      // console.log("images:", typeof(images));
    }

    async function addBook() {
      // const fd = new FormData();
      fd.append("title", bookForm.title);
      // fd.append("author", bookForm.author);
      // fd.append("category", bookForm.category);
      fd.append("author", [this.author]);
      fd.append("category", [this.category]);
      fd.append("condition", bookForm.condition);
      fd.append("language", bookForm.language);
      fd.append("description", bookForm.description);
      // fd.append("image", images);
      // console.log("fd:", fd.entries);

      // bookForm.author.push(author.value);
      // bookForm.category.push(category.value);

      console.log("fd:", fd);
      userStore.addBook(fd, bookForm.shelf);
      // userStore.addBook(fd);
    }

    return {
      chosenLanguage,
      conditions,
      categories,
      Languages,
      bookForm,
      author,
      category,
      updateFiles,
      getLangfullName,
      addBook,
    };
  },

  methods: {},
};
</script>

<style scoped></style>
