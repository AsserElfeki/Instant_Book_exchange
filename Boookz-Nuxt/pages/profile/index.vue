<template>
  <div class="">
    <div
      class="header flex flex-col justify-between items-center py-1 pt-4 md:py-8 rounded-md min-w-full"
    >
      <img
        v-if="profilePic"
        :src="profilePic"
        alt="profile avatar"
        class="w-32 h-32 rounded-full"
      />
      <img
        v-show="!profilePic"
        src="../../assets/img/avatar.png"
        alt="profile avatar"
        class="w-32 h-32 rounded-full"
      />

      <h2 class="text-white md:text-2xl md:font-bold">
        {{ userStore.userName }}
      </h2>
      <h3 class="text-white">{{ userStore.region }}</h3>

      <div
        class="md:mt-8 bg-white rounded-md h-24 flex flex-col md:flex-row justify-center items-center w-10/12"
      >
        <v-toolbar
          color="transparent"
          class="w-full"
        >
          <v-tabs
            dark
            background-color=""
            grow
            vertical
            mobile-break-point="600px"
            class="flex flex-col"
            center-active
          >
            <v-tab @click="activeTab = 'Giveaway'">
              <v-badge
                floating
                color="rgb(167 139 250)"
                :content="`${userStore.userGiveAwayBooks.length}`"
                max="9"
                class="text-xs md:text-lg"
              >
                Giveaway
              </v-badge>
            </v-tab>

            <v-tab @click="activeTab = 'Wanted'">
              <v-badge
                floating
                color="rgb(167 139 250)"
                :content="`${userStore.userWantedBooks.length}`"
                max="9"
                class="text-xs md:text-lg"
              >
                Wanted
              </v-badge>
            </v-tab>

            <v-tab @click="activeTab = 'Transactions'">
              <v-badge
                floating
                color="rgb(167 139 250)"
                :content="`${userStore.userTransactions.length}`"
                max="9"
                class="text-xs md:text-lg"
              >
                Transactions
              </v-badge>
            </v-tab>

            <v-tab @click="activeTab = 'Ratings'">
              <v-badge
                floating
                color="rgb(167 139 250)"
                :content="`${userStore.userRatings.length}`"
                max="9"
                class="text-xs md:text-lg"
              >
                Ratings
              </v-badge>
            </v-tab>
          </v-tabs>
        </v-toolbar>
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
  import { useUserStore } from '~/stores/userStore';
  definePageMeta({
    middleware: 'auth',
  });
  const userStore = useUserStore();
  await userStore.getUserInfo();
  const activeTab = ref('Giveaway');

  const profilePic = userStore.userProfileImage;

  function toggleTabs(event) {
    this.activeTab = event.target.innerText;
  }

  onBeforeMount(() => {
    userStore.getUserInfo();
  });
</script>

<style scoped>
  .header {
    /* height: 500px; */
    background: linear-gradient(93.97deg, #695ac9 0.68%, #925ac9 98.66%);
  }

  .active {
    background: #d4cdff;
  }
</style>
