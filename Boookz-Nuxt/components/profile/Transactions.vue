<template>
  <div class="container">
    <div v-for="transaction in store.userTransactions">
      <h2>Date: {{ transaction.date }}</h2>
        <h2>Transaction with: {{ transaction.book_owner.at(0) }}</h2>
      <div class="bg-[#F2F0FE] rounded-xl p-4 flex flex-col gap-2">
        <div class="flex justify-between bg-white border border-dashed border-black rounded-xl p-4">
          <h3>{{ transaction.title }}</h3>
          <h3>{{ transaction.author.at() }}</h3>
       <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" 
       class="text-green-500 fa-xl"/>
        </div>
        <div class="flex justify-between bg-white border border-dashed border-black rounded-xl p-4">
          <h3>{{ transaction.title }}</h3>
          <h3>{{ transaction.author.at() }}</h3>
          <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket"   class="rotate-180 text-red-500 fa-xl"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const store = useUserStore();
store.getUserHistory();
</script>

<style scoped></style>
