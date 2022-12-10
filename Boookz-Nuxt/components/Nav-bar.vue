<template>
  <nav>
    <ul>
      <li>
        <NuxtLink to="/home">
          <AppLogo />
        </NuxtLink>
      </li>
      <li>
        <NuxtLink to="/signin">Sign in</NuxtLink>
      </li>
      <li>
        <NuxtLink to="/register">Sign up</NuxtLink>
      </li>
    </ul>
  </nav>
</template>

<script setup>

</script>

<style  scoped>
a:hover {
  color: green;
}
</style>