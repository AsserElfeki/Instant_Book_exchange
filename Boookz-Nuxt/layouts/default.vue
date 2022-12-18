<template>
  <div class="wrapper">
    <div class="content-wrapper">
      <Nav-bar />
      <div class="content">
        <!-- this where the page components go -->
        <slot />
      </div>
      <AppFooter />
    </div>
  </div>

</template>

<script setup>
import { useStore } from '~/stores/store'
const store = useStore()
//running it here so it always runs and I dont have to call it inside each component/page
store.getBooksFromDB()
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


</style>





