<template>
  <div class="">
    <v-menu min-height="1000px">
      <template v-slot:activator="{ props: menu }">
        <v-tooltip location="top">
          <template v-slot:activator="{ props: tooltip }">
            <v-btn
              :color="store.notifications?.length > 0 ? 'red' : 'white'"
              v-bind="mergeProps(menu, tooltip)"
              class="relative"
            >
              <font-awesome-icon
                icon="fa-regular fa-bell"
                class="fa-2x"
              />
              <v-badge
                v-if="store.notifications?.length > 0"
                class="absolute bottom-1 right-0"
                color="white"
                :content="`${store.notifications.length}`"
                max="9"
              >
              </v-badge>
            </v-btn>
          </template>
          <span>Notifications</span>
        </v-tooltip>
      </template>
      <v-list class="">
        <v-list-item
          v-for="(item, index) in store.notifications"
          :key="index"
          class="hover:bg-violet-300 rounded-xl hover:cursor-pointer"
        >
          <v-list-item-title @click="handleNotification(item.pk)">{{
            item.content
          }}</v-list-item-title>
        </v-list-item>
        <v-list-item
          v-if="store.notifications?.length !== 0"
          class="rounded-xl flex justify-center"
        >
          <v-btn
            class="hover:cursor-pointer hover:bg-violet-300 rounded-xl mb-2"
            @click="clearNotifications"
            >clear all</v-btn
          >
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script setup>
  import { mergeProps } from 'vue';
  import { useUserStore } from '~/stores/userStore';

  const store = useUserStore();

  async function handleNotification(notificationPK) {
    store.deleteNotification(notificationPK);
    // await navigateTo("/profile");
  }

  function clearNotifications() {
    store.clearNotifications();
  }
</script>
