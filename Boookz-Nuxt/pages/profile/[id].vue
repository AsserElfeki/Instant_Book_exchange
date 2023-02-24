<template>
  <div class="">
    <div
      class="header flex flex-col justify-between items-center py-1 pt-4 md:py-8 rounded-md "
    >
      <img
        v-if="userStore.userProfileImage"
        :src="userStore.userProfileImage"
        alt="profile avatar"
        class="w-32 h-32 rounded-full"
      />
      <img
        v-else
        src="../../assets/img/avatar.png"
        alt="profile avatar"
        class="w-32 h-32 rounded-full"
      />

      <h2 class="text-white font-sans md:text-2xl md:font-bold">
        {{ userStore.userName }}
      </h2>
      <h3 class="text-white font-sans font-thin">{{ userStore.region }}</h3>

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
      <LazyProfileRatings v-if="activeTab === 'Ratings'" />
    </div>
  </div>
</template>

<script setup>
import { useProfileStore } from "~/stores/profileStore";
definePageMeta({
  middleware: "auth",
});
const userStore = useProfileStore();
const route = useRoute().params;
userStore.userName = route.id;
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
  width: 100%;
  background: linear-gradient(93.97deg, #695ac9 0.68%, #925ac9 98.66%);
}

.active {
  background: #d4cdff;
}
</style>
