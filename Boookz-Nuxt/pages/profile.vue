<template>
  <div class="">
    <div
      class="header flex flex-col justify-between items-center py-1 md:py-8 rounded-md border-4 border-red-700"
    >
      <img src="../assets/img/avatar.png" alt="profile avatar" class="" />
      <h2 class="text-white font-sans md:text-2xl md:font-bold">
        {{ userStore.userName }}
      </h2>
      <h3 class="text-white font-sans font-thin">{{ userStore.region }}</h3>

      <div
        class="md:mt-8 md:bg-white rounded-md h-24 flex flex-col md:flex-row justify-around items-center"
      >
        <button
          class="md:mx-7 md:w-18 md:h-20 px-2 rounded-md"
          :class="{ active: activeTab === 'Giveaway' }"
          @click="toggleTabs($event)"
        >
          Giveaway
        </button>
        <button
          class="md:mx-7 md:w-18 md:h-20 px-2 rounded-md"
          :class="{ active: activeTab === 'Wanted' }"
          @click="toggleTabs($event)"
        >
          Wanted
        </button>
        <button
          class="md:mx-7 md:w-18 md:h-20 px-2 rounded-md"
          :class="{ active: activeTab === 'Transactions' }"
          @click="toggleTabs($event)"
        >
          Transactions
        </button>
        <button
          class="md:mx-7 md:w-18 md:h-20 px-2 rounded-md"
          :class="{ active: activeTab === 'Ratings' }"
          @click="toggleTabs($event)"
        >
          Ratings
        </button>
      </div>
    </div>

    <div class="content">
      <LazyProfileGiveaway v-if="activeTab === 'Giveaway'" />
      <LazyProfileWanted v-if="activeTab === 'Wanted'" />
      <LazyProfileTransactions v-if="activeTab === 'Transactions'" />
      <LazyProfileRatings v-if="activeTab === 'Ratings'" />
    </div>
  </div>
</template>

<script setup>
// import { LazyProfileRatings, LazyProfileTransactions } from '~/.nuxt/components';
import { useUserStore } from "~/stores/userStore";
definePageMeta({
  middleware: "auth",
});
const userStore = useUserStore();

const activeTab = ref("");

function toggleTabs(event) {
  this.activeTab = event.target.innerText;
}

// await userStore.getUserInfo();

</script>

<style scoped>
.header {
  /* height: 500px; */
  width: 100%;
  background: linear-gradient(93.97deg, #695ac9 0.68%, #925ac9 98.66%);
}

.active {
  background: #d4cdff;
}
</style>
