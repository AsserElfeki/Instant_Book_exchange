<template>
  <div v-if="store.userRatings.length" class="flex flex-col gap-4 justify-center">
    <h2 class="font-bold text-xl font-sans m-2">My Reviews</h2>
    <div
      v-for="rating in store.userRatings"
      :key="rating.id"
      class="border border-dashed border-black rounded-2xl p-4"
    >
      <div class="font-sans">
        <img src="rating.image" alt="profile picture of the user who made the rating" />
        <h3 class="inline text-xl font-bold font-sans">person {{ rating.name }}</h3>
        <h3 class="inline">rated with {{ rating.stars }}</h3>
        <p>comment: {{ rating.comment }}</p>
        <p>date: {{ rating.date }}</p>
      </div>
    </div>
  </div>

  <div v-else class="mt-16">
    <LazyProfilePlaceHolder />
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const store = useUserStore();
// await store.getUserInfo();
</script>
