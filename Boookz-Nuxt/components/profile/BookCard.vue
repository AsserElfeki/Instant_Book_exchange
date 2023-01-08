<template>
  <div
    class="bg-[#dddaee] max-w-xs shadow-xl relative rounded-3xl py-1 md:p-3 h-full max-h-96"
  >
    <div class="rounded-3xl  max-h-[800px] flex flex-col gap-2 justify-between p-2  h-full">
      <img
        :src="book.images.at(0)"
        :alt="book.title"
        class="w-full rounded-3xl max-h-40 md:max-h-72 object-contain md:min-h-[250px]"
      />

      <p class="text-[#e76f51] text-md md:text-lg max-h-20">{{ truncate(book.title, 50) }}</p>
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
.selected {
  background-color: #ddd;
  border: 2px solid #333;
}
</style>
