<template>
  <div v-if="store.userRatings.length" class="flex flex-col gap-4 justify-center px-2">
    <h2 v-if="route.id" class="font-bold text-xl  m-2">{{store.userName}}'s Reviews</h2>
    <h2 v-else class="font-bold text-xl  m-2">My Reviews</h2>
    <div
      v-for="rating in store.userRatings"
      :key="rating.pk"
      class="border border-dashed border-black rounded-2xl p-4"
    >
      <div class="">
        <img
          :src="rating.book_reader.profile_image"
          alt="profile picture of the user who made the rating"
          class="rounded-full w-12 h-12 inline mr-4"
        />
        <h3 class="inline text-xl font-bold "> {{ rating.book_reader.username }} </h3>
        <h3 class="inline"> rated with {{ rating.rating }}</h3>
        <p>comment: {{ rating.comment }}</p>
        <p>date: {{ rating.modified }}</p>
      </div>
    </div>
  </div>

  <div v-else class="mt-16">
    <LazyProfilePlaceHolder />
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
import { useProfileStore } from "~/stores/profileStore";
const route = useRoute().params;
const store = !route.id ? useUserStore() : useProfileStore();
// await store.getUserInfo();
</script>
