<template>
  <div
    class="flex flex-col gap-3 mx-5 my-9 justify-between items-center lg:flex-row relative"
  >
    <NuxtLink
      to="/"
      class="flex gap-2 justify-start self-start"
      active-class="inactive"
    >
      <AppLogo />
      <div class="gap-8">
        <h1 class="hi font-bold text-[33px] leading-10 h-9 font-segoe">
          Boookz
        </h1>
        <p class="text-xs">Book xchange website</p>
      </div>
    </NuxtLink>
    <div class="flex my-auto items-center relative">
      <form @submit.prevent="search">
        <input
          placeholder="Search"
          type="text"
          class="bg-gray-100 rounded-lg px-3 w-60 md:w-96 h-8"
          v-model="searchQuery"
        />
        <button
          class=""
          type="submit"
        >
          <img
            src="/MagnifyingGlass.png"
            alt="search icon"
            class="absolute top-0 right-2"
          />
        </button>
      </form>
    </div>
    <ul
      v-if="!store.userIsLoggedIn"
      class="flex flex-row gap-6 lg:gap-2 "
    >
      <NuxtLink
        class="btn-sm lg:btn"
        to="/signin"
        >Sign in</NuxtLink
      >
      <NuxtLink
        class="btn-sm lg:btn"
        to="/register"
        >Sign up</NuxtLink
      >
    </ul>

    <ul
      v-else
      class="flex gap-8 justify-center items-center "
    >
      <img
        v-if="store.userProfileImage"
        :src="store.userProfileImage"
        alt="profile avatar"
        class="w-8 h-8 rounded-full"
        @click="redirect"
      />
      <img
        v-else
        src="../assets/img/avatar.png"
        alt="profile avatar"
        class="w-8 h-8 rounded-full"
        @click="redirect"
      />
      <ProfileSettingMenu />
      <ProfileNotificationMenu />
    </ul>
  </div>
</template>

<script>
  import { useGoogleAPIStore } from '~/stores/googleAPIStore';
  import { useUserStore } from '~/stores/userStore';

  import 'vuetify/styles';
  import { createVuetify } from 'vuetify';
  import * as components from 'vuetify/components';
  import * as directives from 'vuetify/directives';

  //here I am using the setup function explicitly, but you can also use the composition API
  //if you need to access some part of state, remember to add it to the return object
  //I Love github copilot <3
  export default {
    setup() {
      const vuetify = createVuetify({
        components,
        directives,
      });

      const googleAPIStore = useGoogleAPIStore();
      const store = useUserStore();

      const notificationshown = ref(false);
      const settingsshown = ref(false);

      const searchQuery = ref('');
      // const userIsLoggedIn = store.userIsLoggedIn

      const search = () => {
        googleAPIStore.searchForBook(searchQuery.value);
      };

      const redirect = () => {
        return navigateTo('/profile');
      };

      const logOut = () => {
        store.logOut();
      };

      // function showSettings() {
      //   notificationshown.value = false;
      //   settingsshown.value = true;
      // }

      // function showNotifications() {
      //   settingsshown.value = false;
      //   notificationshown.value = true;
      // }

      return {
        searchQuery,
        googleAPIStore,
        search,
        store,
        logOut,
        redirect,
        notificationshown,
        settingsshown,
      };
    },
  };
</script>

<style scoped>
  .hi {
    font-family: 'Segoe';
  }
</style>
