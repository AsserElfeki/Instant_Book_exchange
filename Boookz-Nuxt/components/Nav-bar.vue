<template>

  <div class="navBar">
    <NuxtLink to="/home">
      <AppLogo />
    </NuxtLink>
    <div class="search-box">
      <input placeholder="Search" type="text" class="search-bar" v-model="searchQuery">
      <button class="" @click="search">
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
import { useGoogleAPIStore } from '~/stores/googleAPIStore';

export default {
  setup() {
    const searchQuery = ref('')
    const googleAPIStore = useGoogleAPIStore()

    const search = () => {
      googleAPIStore.searchForBook(searchQuery.value)
    }

    return { searchQuery, googleAPIStore, search }
  }
}


</script>

<style  scoped>

</style>

// ToDO : 
// 1. Add a search bar ✅
// 2. Add a search button ✅
// 3. Add a search function ✅
// 6. Add a search result component to the home page
// 7. get authentication status and display nav bar accordingly
