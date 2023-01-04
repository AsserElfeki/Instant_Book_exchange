<template>
  <div
    class="bg-[#dddaee] my-4 max-w-xs shadow-xl relative rounded-3xl flex flex-col items-center overflow-visible p-3 "
  >
    <div class="rounded-3xl w-full max-h-[800px]">
      <img
        :src="book.images.at(0)"
        :alt="book.title"
        class="cover rounded-3xl w-full max-h-40 object-contain"
      />

      <h4 class="text-[#e76f51] text-center text-sm md:text-xl h-20 overflow-hidden">
        {{ truncate(book.title, 28) }}
      </h4>
    </div>
    <div class="flex justify-between mb-3 min-w-full ">
      <p class="text-sm md:text-lg mb-1">by: {{ book.book_owner.username }}</p>
    </div>
    <img
      :src="book.book_owner.profile_image"
      :alt="book.book_owner.username"
      class="user-image w-16 h-16 rounded-full object-cover absolute bottom-[-40px] left-1/2 -translate-x-1/2 border-black border"
    />
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const { book } = defineProps(["book"]);
const store = useUserStore();
function truncate(string, value) {
  if (string.length > value) return string.substring(0, value) + "…";
  else return string;
}
</script>

<style scoped></style>
