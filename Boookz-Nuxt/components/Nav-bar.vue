<template>
  <nav>
    <div class="navBar">
      <NuxtLink to="/home">
        <AppLogo />
      </NuxtLink>

      <ul class="flex flex-row ">
        <li class="mr-7 btn">
          <NuxtLink to="/signin">Sign in</NuxtLink>
        </li>
        <li class="btn">
          <NuxtLink to="/register">Sign up</NuxtLink>
        </li>
      </ul>
    </div>

  </nav>
</template>

<script setup>

</script>

<style  scoped>
a:hover {
 
}
</style>