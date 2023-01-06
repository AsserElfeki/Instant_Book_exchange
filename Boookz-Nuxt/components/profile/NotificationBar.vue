<template>
  <div class="border-2 border-black">
    <button @click="showMenu = !showMenu" class="">
    <font-awesome-icon icon="fa-regular fa-bell" 
    class="fa-xl"/>
    </button>
    <ul v-if="showMenu" class="notification-menu">
      <li v-for="notification in userStore.notifications">{{ notification.content }}</li>
    </ul>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const userStore = useUserStore();
const showMenu = ref(true);
</script>

<style scoped></style>
