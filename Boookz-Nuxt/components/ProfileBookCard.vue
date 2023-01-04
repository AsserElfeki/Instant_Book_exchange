<template>
  <div
    class="bg-[#dddaee] my-4 max-w-xs shadow-xl relative rounded-3xl flex flex-col items-center overflow-visible p-3"
  >
    <div class="rounded-3xl w-full max-h-[800px]">
      <img
        :src="book.images.at(0)"
        :alt="book.title"
        class="cover rounded-3xl w-full max-h-40 object-contain"
      />

      <p class="text-[#e76f51] text-sm md:text-xl h-20">{{ truncate(book.title, 30) }}</p>
   
    </div>
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

<style scoped>

</style>
