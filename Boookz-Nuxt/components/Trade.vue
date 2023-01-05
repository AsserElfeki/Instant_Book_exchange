<template>
  <div>
    <p>Choose the book to exchnage</p>
    <div v-if="store.userGiveAwayBooks.length" 
    class="flex flex-col items-center justify-center w-full mx-auto px-4">
      <h2 class="font-bold text-xl font-sans m-2 self-start">My Giveaway Books</h2>
      <div class="flex gap-2 items-stretch">
          <div 
            class="flex-1"
            :class="{ 'selected': book }"
            v-on:click="toggleSelect"
            v-for="book in store.userGiveAwayBooks">
            <ProfileBookCard :book="book" />
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "~/stores/userStore";
import { useDataStore } from "~/stores/dataStore";


export default {
  methods: {
    toggleSelect() {
      console.log("toggleSelect");
    }
  },
  setup() {
  const store = useUserStore();
  const dataStore = useDataStore();
  return { store, dataStore };
}

}
</script>

<style scoped>

</style>
