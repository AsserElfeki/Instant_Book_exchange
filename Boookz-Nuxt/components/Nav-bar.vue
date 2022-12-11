<template>

  <div class="navBar">
    <NuxtLink to="/home">
      <AppLogo />
    </NuxtLink>
    <div class="search-box">
      <input placeholder="Search" type="text" class="search-bar">
      <button class="">
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

<script setup>

</script>

<style  scoped>

</style>