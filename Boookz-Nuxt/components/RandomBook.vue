<template>
  <div class="container flex flex-col justify-center items-center rounded-2xl p-3 gap-3">
    <h3 class="self-start text-[#695AC9]">#suggested for YOU</h3>

    <div class="flex justify-around items-center flex-row gap-3 md:gap-20 ">
      <div class="rounded-md max-h-[400px]">
        <img
          v-if="book.images"
          class="rounded-md w-full min-w-[200px] max-w-sm max-h-[400px]"
          :src="book.images.at(0)"
          alt="cover of the book"
        />
      </div>

      <div class="flex flex-col gap-4">
        <h3 class="text-xl text-black text-center">{{ book.title }}</h3>
        <h3 class="text-left text-md">By:</h3>
        <div>
          <p v-for="author in book.author" :key="author" class="">{{ author }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const { book } = defineProps(["book"]);

console.log("random book:", book);
</script>

<style scoped>
.container {
  background-image: url("../assets/img/heroBackground.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  /* height: 400px; */
}
</style>
