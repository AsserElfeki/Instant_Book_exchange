<template>
  <div class="flex flex-col m-0 p-0 border-2 relative">
    <button @click="showMenu = !showMenu" class="">
      <font-awesome-icon  icon="fa-solid fa-gear" class="fa-xl" />
    </button>
    <div v-if="showMenu" class="flex flex-col absolute top-8">
      <p v-for="item in menuItems">{{ item }}</p>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const userStore = useUserStore();
const showMenu = ref(false);

const menuItems = {
    "Settings": "settings",
    "Log out": "logOut"
}

</script>

<style scoped></style>
