<template>
  <div>
    <h1>Welcome from home page</h1>

    <div v-for="p in products">
      <NuxtLink :to="`/books/${p.id}`">{{ p.title }}</NuxtLink>
    </div>
  </div>
</template>

<script setup>

//this function can fire both on server and on the browser
// fetch the products 
//save the data in variable called products
const { data: products } = await useFetch("https://fakestoreapi.com/products ")
</script>

<style lang="scss" scoped>

</style>