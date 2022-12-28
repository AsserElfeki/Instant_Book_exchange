<template>
  <div class="wrapper">
    <div class="content-wrapper">
      <NavigationBar class="" />

      <div class="content">
        <!-- this where the page components go -->
        <slot />
      </div>
    </div>
  </div>
  <AppFooter />
</template>

<script setup>
import { useDataStore } from "~~/stores/dataStore";
const store = useDataStore();
//running it here so it always runs and I dont have to call it inside each component/page
store.getOfferedBooksFromDB();
store.getWantedBooksFromDB();
</script>

<style>
html {
  font-family: "Mulish", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  /* border: 2px solid red; */
}

/* exact link will show the primary color for only the exact matching link */
.router-link-exact-active {
  background-color: #695ac9;
  color: white;
  box-shadow: 3px 3px 3px rgb(114, 114, 114);
}

.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
