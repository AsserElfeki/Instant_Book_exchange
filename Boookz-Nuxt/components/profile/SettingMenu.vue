<template>
  <div class="">
    <v-menu>
      <template v-slot:activator="{ props: menu }">
        <v-tooltip location="top">
          <template v-slot:activator="{ props: tooltip }">
            <v-btn v-bind="mergeProps(menu, tooltip)">
              <font-awesome-icon
                icon="fa-solid fa-gear"
                class="fa-2x"
              />
            </v-btn>
          </template>
          <span>Settings</span>
        </v-tooltip>
      </template>
      <v-list>
        <v-list-item @click="goToSettings">
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item>

        <v-list-item @click="logOut">
          <v-list-item-title>LogOut</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script setup>
  import { mergeProps } from 'vue';
  import { useUserStore } from '~/stores/userStore';
  import { useDataStore } from '~/stores/dataStore';

  const dataStore = useDataStore();
  const {$toast} = useNuxtApp();

  const store = useUserStore();

  async function goToSettings() {
    await navigateTo('/user/settings');
  }

  async function logOut() {
    store.logOut();
    await dataStore.updateData();
    $toast.success('You are logged out', {
      timeout: 5000,
    });
  }
</script>
