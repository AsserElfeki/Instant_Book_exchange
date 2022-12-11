<template>
  <div class="wrapper">
    <div class="content-wrapper">
      <Nav-bar />
      <div class="content">
        <!-- this where the page components go -->
        <slot />
      </div>
      <AppFooter></AppFooter>
    </div>
  </div>

</template>

<script setup>
import { useStore } from '~/stores/store'
const store = useStore()
store.retrieveBook()
</script>

<style>
html {
  font-family: "Mulish", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  /* font-size: 16px; */
  /* word-spacing: 1px; */
  /* -ms-text-size-adjust: 100%; */
  /* -webkit-text-size-adjust: 100%; */
  /* -moz-osx-font-smoothing: grayscale; */
  /* -webkit-font-smoothing: antialiased; */
  box-sizing: border-box;
  /* line-height: 1.4; */
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
  border: 2px solid red;
}
</style>





