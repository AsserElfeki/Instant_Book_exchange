<template>
  <div
    class="container flex flex-col justify-center items-center rounded-2xl p-3 gap-3 mx-auto"
  >
    <h3 class="self-start text-[#695AC9]">#suggested for YOU</h3>

    <div class="flex flex-col md:flex-row justify-evenly items-center gap-3 md:gap-20 w-full">
      <div class=" max-h-[400px] ">
        <NuxtLink
          :to="`/books/${book.title}`"
          @click.left="store.setClickedBook(book)"
          @click.middle="store.setClickedBook(book)"
          @click.right="store.setClickedBook(book)"
        >
          <img
            v-if="book.images"
            class="rounded-md  min-w-[200px] max-w-sm max-h-[400px]"
            :src="book.images.at(0)"
            alt="cover of the book"
          />
        </NuxtLink>
      </div>

      <div class="flex flex-col gap-4">
        <h3 class="text-2xl text-black">{{ book.title }}</h3>
        <div>
          <h3 class="text-left text-md text-xl">By:</h3>
          <p
            v-for="author in book.author"
            :key="author"
            class="text-xl"
          >
            {{ author }}
          </p>
        </div>
        <p class="text-violet-700 text-lg">{{ book.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useDataStore } from '~/stores/dataStore';
  const store = useDataStore();

  const { book } = defineProps(['book']);

  console.log('random book:', book);
</script>

<style scoped>
  .container {
    background-image: url('../assets/img/heroBackground.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    /* height: 400px; */
  }
</style>
