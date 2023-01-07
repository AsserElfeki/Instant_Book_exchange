<template>
  <div class="flex flex-col justify-center items-center">
    <form @submit.prevent="addBook" enctype="multipart/form-data"
      class="flex flex-col justify-center gap-3 w-full sm:w-3/5 lg:w-1/2 mx-auto p-2">
      <fieldset class="flex justify-between">
        <label for="shelf">Shelf:</label>
        <select id="shelf" v-model="bookForm.shelf"
          class="border-2 rounded-md overflow-y-scroll max-h-12 w-44 text-center">
          <option value="" disabled>-Select Shelf-</option>
          <option value="giveaway">Giveaway shelf</option>
          <option value="wanted">Wanted shelf</option>
        </select>
      </fieldset>

      <fieldset class="flex justify-between">
        <label for="language">Language:</label>
        <select id="language" v-model="chosenLanguage" @change="getLangfullName" size="1"
          class="border-2 rounded-md overflow-y-scroll max-h-12 w-44 text-center">
          <option value="" disabled>-Select Language-</option>

          <option v-for="language in Languages" :key="language" :value="language">
            {{ language }}
          </option>
        </select>
      </fieldset>


      <label for="book-title" class="self-start">Book title:</label>
      <v-autocomplete
          :items="suggestedTitles"
          v-model="bookForm.title"
          @input="getTitleUsingGoogleAPI"
          no-filter
          size="40"
          id="book-title"
          type="text"
          placeholder="Book title"
      />


      <label for="book-author" class="self-start">Authors:</label>
      <div v-if="bookForm" v-for="(author_at, index) in bookForm.author" :key="index">
        <div class="w-full flex justify-between">
          <v-text-field class=" w-96 inline" label="Book author" v-model="bookForm.author[index]"></v-text-field>

          <button class="btn btn-danger w-14 h-14 ml-3" @click="deleteAuthorField(index)">
            <img src="../../assets/img/trash-bin.png" alt="Delete" /> </button>

        </div>
      </div>
      <button type="button" class="btn btn-primary w-14 h-14 items-center" @click="addAuthorField">+</button>
      <label for="category">Category(s):</label>

      <div class="flex justify-between gap-6">
        <v-combobox label="category" :items="categories" v-model="bookForm.category" variant="solo"
          class=" p-2 rounded-md" multiple></v-combobox>
      </div>

      <div class="flex justify-between gap-6">
        <label for="condition">Condition:</label>
        <select id="condition" v-model="bookForm.condition" size="1"
          class="overflow-y-scroll h-auto border-2 rounded-md w-44 text-center">
          <option value="" disabled>-Select Condition-</option>
          <option v-for="condition in conditions" :key="condition" :value="condition">
            {{ condition }}
          </option>
        </select>
      </div>

      <label for="book-images" class="self-start">upload images:</label>
      <input id="book-images" type="file" multiple accept=".png, .jpg, .jpeg, .heic"
        @change="updateFiles($event.target.files)" class="border p-2 rounded-md" />

      <button type="submit" class="btn-sm self-center">add book</button>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
import { useLangAPIStore } from "~/stores/languagesStore";
import {useGoogleAPIStore} from "~/stores/googleAPIStore";

const userStore = useUserStore();
const langStore = useLangAPIStore();
const googleStore = useGoogleAPIStore();

const Languages = langStore.getAllLanguages();

const conditions = ["Bad", "Perfect", "Good"];
const categories = ["fiction", "romance", "science"];

const chosenLanguage = ref("");
const suggestedTitles = ref([]);
// const suggestedImage = ref("");

const fd = new FormData();

const bookForm = reactive({
  title: "",
  author: [],
  category: [],
  condition: "",
  language: "",
  image: [],
  description: "some description",
  shelf: "",
});
async function getTitleUsingGoogleAPI(event) {
      bookForm.title = event.target.value
      const languageCode = langStore.chosenLangCode
      if (bookForm.title.length > 0){
        await googleStore.searchForBookTitles(bookForm.title, languageCode);
        suggestedTitles.value = googleStore.book_titles;
      }
}

// async function getBookImageUsingGoogleAPI() {
//   const languageCode = langStore.chosenLangCode
//   console.log("TEST")
//   console.log(bookForm.title)
//
//   if (bookForm.title.length > 0){
//     await googleStore.getBookThumbnailFromTitle(bookForm.title, languageCode);
//     suggestedImage.value = googleStore.book_image;
//     console.log(suggestedImage.value)
//   }
// }
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
  if (bookForm.shelf) {
    fd.append("title", bookForm.title);
    fd.append("author", bookForm.author);
    fd.append("category", bookForm.category);
    fd.append("condition", bookForm.condition);
    fd.append("language", bookForm.language);
    fd.append("description", bookForm.description);

    console.log("fd:", fd);
    console.log("bookForm:", bookForm);
    userStore.addBook(fd, bookForm.shelf);
    fd.delete("image");
    fd.delete("title");
    fd.delete("author");
    fd.delete("category");
    fd.delete("condition");
    fd.delete("language");
    fd.delete("description");
  
  }
  else {
    alert("please select a shelf")
  }
}
function addAuthorField() {
  bookForm.author.push("");
}

function deleteAuthorField(index) {
  bookForm.author.splice(index, 1);
}

</script>

<style scoped>
input {
  border: 2px solid black;
  border-radius: 7px;
  padding: 10px;
}
</style>
