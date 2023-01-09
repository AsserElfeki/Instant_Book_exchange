<template>
  <div
    class="flex flex-col mx-5 gap-2 items-center lg:flex-row justify-between w-full relative"
  >
    <NuxtLink
      to="/"
      class="flex gap-2 justify-center self-start items-start"
      active-class="inactive"
    >
      <AppLogo />
      <div class="flex flex-col justify-start">
        <h1 class="font-bold text-[33px] leading-10 h-9">Boookz</h1>
        <p class="leading-none">Book xchange website</p>
      </div>
    </NuxtLink>
    <div class="flex my-auto items-center relative">
      <form @submit.prevent="search">
        <input
          placeholder="Search offered books"
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
      class="flex flex-row gap-6 lg:gap-2 self-end"
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
      class="flex gap-8 justify-center items-center self-end lg:self-auto"
    >
      <img
        v-if="store.userProfileImage"
        :src="store.userProfileImage"
        alt="profile avatar"
        class="w-8 h-8 rounded-full hover:cursor-pointer"
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
  import { useDataStore } from '~/stores/dataStore';

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
      const dataStore = useDataStore();
      const store = useUserStore();

      const notificationshown = ref(false);
      const settingsshown = ref(false);

      const searchQuery = ref('');
      // const userIsLoggedIn = store.userIsLoggedIn

      const search = () => {
        // googleAPIStore.searchForBook(searchQuery.value);
        dataStore.searchForBook(searchQuery.value);
        searchQuery.value = '';
      };

      const redirect = () => {
        return navigateTo('/profile');
      };

      const logOut = () => {
        store.logOut();
      };

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

<style scoped></style>
