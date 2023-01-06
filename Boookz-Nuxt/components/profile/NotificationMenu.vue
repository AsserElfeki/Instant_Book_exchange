<template>
  <div class="flex m-0 p-0 border-2">
    <button @click="showMenu = !showMenu" class="">
      <font-awesome-icon  icon="fa-regular fa-bell" class="fa-xl" />
    </button>
    <ul v-if="showMenu" class="">
      <li v-for="notification in userStore.notifications">{{ notification.content }}</li>
    </ul>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const userStore = useUserStore();
const showMenu = ref(false);
</script>

<style scoped></style>
