<template>
  <div v-if="store.userTransactions.length" class="flex flex-col gap-4 justify-center">
    <h2 class="font-bold text-xl font-sans m-2">My History</h2>
    <div
      v-for="transaction in store.userTransactions"
      :key="transaction.token"
      class="flex flex-col gap-2 m-2"
    >
      <h2>Date: {{ transaction.created }}</h2>
      <!-- <h2>Initiated By: {{ transaction.book_reader_initiator.username }}</h2> -->
      <div class="bg-[#F2F0FE] rounded-xl p-4 flex flex-col gap-2">
        <div
          class="flex flex-row md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg font-segoe">
            {{ transaction.book_reader_initiator.username }}
          </h3>
          <h3 class="font-bold text-lg font-mono">
            {{ transaction.initiator_book.title }}
          </h3>
          <font-awesome-icon
            v-if="transaction.book_reader_initiator.username === store.userName"
            icon="fa-solid fa-arrow-right-from-bracket"
            class="text-green-500 fa-xl"
          />
          <font-awesome-icon
            v-else
            icon="fa-solid fa-arrow-right-from-bracket"
            class="rotate-180 text-red-500 fa-xl"
          />
          <!-- sadsad  -->
        </div>
        <div
          class="flex flex-row md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg font-segoe">
            {{ transaction.book_reader_receiver.username }}
          </h3>
          <h3 class="font-bold text-lg font-mono">
            {{ transaction.receiver_book.title }}
          </h3>
          <font-awesome-icon
            v-if="!transaction.book_reader_initiator.username === store.userName"
            icon="fa-solid fa-arrow-right-from-bracket"
            class="text-green-500 fa-xl"
          />
          <font-awesome-icon
            v-else
            icon="fa-solid fa-arrow-right-from-bracket"
            class="rotate-180 text-red-500 fa-xl"
          />
        </div>
        <h2 class="self-center text-violet-700 font-sans font-bold">
          Status: {{ transaction.transaction_status }}
        </h2>
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
</script>

<style scoped></style>
