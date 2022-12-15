<template>
  <div>
    <h1 class="text-3xl flex justify-center ">Welcome from home page</h1>

    <div class="mt-4">
    <div v-for="p in products" class="flex flex-col justify-center items-center mt-1">
      <NuxtLink :to="`/books/${p.id}`">{{ p.title }}</NuxtLink>
    </div>
    </div>  
    

  </div>
</template>

<script setup>

//this function can fire both on server and on the browser
// fetch the products 
//save the data in variable called products
const { data: products } = await useFetch("http://localhost:4000/books")
</script>

<style lang="scss" scoped>

</style>