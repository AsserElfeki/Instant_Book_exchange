<template>
  <div v-if="store.userTransactions.length" class="flex flex-col gap-4 justify-center">
    <h2 class="font-bold text-xl font-sans m-2">My History</h2>
    <div
      v-for="transaction in store.userTransactions"
      :key="transaction.id"
      class="flex flex-col gap-2 m-2"
    >
      <h2>Date: {{ transaction.date }}</h2>
      <h2>Transaction with: {{ transaction.book_owner.at(0) }}</h2>
      <div class="bg-[#F2F0FE] rounded-xl p-4 flex flex-col gap-2">
        <div
          class="flex flex-col md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg font-segoe">{{ transaction.title }}</h3>
          <h3>{{ transaction.author.at() }}</h3>
          <font-awesome-icon
            icon="fa-solid fa-arrow-right-from-bracket"
            class="text-green-500 fa-xl"
          />
        </div>
        <div
          class="flex flex-col md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg font-segoe">{{ transaction.title }}</h3>
          <h3>{{ transaction.author.at() }}</h3>
          <font-awesome-icon
            icon="fa-solid fa-arrow-right-from-bracket"
            class="rotate-180 text-red-500 fa-xl"
          />
        </div>
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
await store.getUserHistory();
</script>

<style scoped></style>
