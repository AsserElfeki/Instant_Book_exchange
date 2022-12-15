<template>

  <div class="navBar">
    <NuxtLink to="/home">
      <AppLogo />
    </NuxtLink>
    <div class="search-box">
      <input placeholder="Search" type="text" class="search-bar" :value="searchQuery">
      <button class="" @click="googleAPIStore.searchForBook(searchQuery)">
        <img src="/MagnifyingGlass.png" alt="search icon" class="absolute top-0 right-2 ">
      </button>
    </div>
    <ul class="flex flex-row ">
      <li class="mr-7 btn">
        <NuxtLink to="/signin">Sign in</NuxtLink>
      </li>
      <li class="btn">
        <NuxtLink to="/register">Sign up</NuxtLink>
      </li>
    </ul>
  </div>

</template>

<script>

//call the googleApiSTore action searchForBooks when the button is presses and pass the value of the input as a param



import { useGoogleAPIStore } from '~/stores/googleAPIStore';
const googleAPIStore = useGoogleAPIStore()
// const searchQuery = ref()

export default {
  data() {
    return {
      searchQuery: 'harry'
    }
  }, methods: {
    searchForBook() {
      googleAPIStore.searchForBook(this.searchQuery)
    }
  }
}

</script>

<style  scoped>

</style>