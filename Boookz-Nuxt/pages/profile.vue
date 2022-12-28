<template>
  <div class="header flex flex-col justify-between items-center py-8 rounded-md">
    <img src="../assets/img/avatar.png" alt="profile avatar" class="" />
    <h2 class="text-white font-sans text-2xl font-bold">{{ userStore.userName }}</h2>
    <h3 class="text-white font-sans font-thin">{{ userStore.region }}</h3>

    <div
      class="tabs mt-8 bg-white rounded-md h-24 w-11/12 flex justify-around items-center"
    >
      <button
        class="tab mx-7 w-18 h-20 px-2 rounded-md"
        :class="{ active: activeTab === 'Giveaway' }"
        @click="toggleTabs($event)"
      >
        Giveaway
      </button>
      <button
        class="tab mx-7 w-18 h-20 px-2 rounded-md"
        :class="{ active: activeTab === 'Wanted' }"
        @click="toggleTabs($event)"
      >
        Wanted
      </button>
      <button
        class="tab mx-7 w-18 h-20 px-2 rounded-md"
        :class="{ active: activeTab === 'Transactions' }"
        @click="toggleTabs($event)"
      >
        Transactions
      </button>
      <button
        class="tab mx-7 w-18 h-20 px-2 rounded-md"
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
</script>

<style scoped>
.header {
  height: 500px;
  width: 100%;
  background: linear-gradient(93.97deg, #695ac9 0.68%, #925ac9 98.66%);
}

.active {
  background: #d4cdff;
}
</style>
