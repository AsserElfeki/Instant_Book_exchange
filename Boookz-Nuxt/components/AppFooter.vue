<template>
  <footer class="mt-8 bg-violet-400">
    <ul class="footer max-w-screen-xl flex justify-between mx-auto py-2">
      
      <li class="hover:text-white border-b-2 border-transparent hover:border-white">
        <a 
        href="https://github.com/AsserElfeki/Instant_Book_exchange" 
        target="_blank"
        class="flex flex-col-reverse"
          >Visit GitHub Repo
          <font-awesome-icon icon="fa-brands fa-github" class="fa-2x" />
        </a>
      </li>

      <li class="hover:text-white border-b-2 border-transparent hover:border-white">
        <a href="https://www.linkedin.com" 
        target="_blank"
        class="flex flex-col-reverse"
          >LinkedIn
          <font-awesome-icon icon="fa-brands fa-linkedin" class="fa-2x " />
        </a>
      </li>

      <li class="hover:text-white border-b-2 border-transparent hover:border-white">
      <NuxtLink 
      to="/about"
      class="flex flex-col-reverse"
      >
      Meet The Team
          <font-awesome-icon icon="fa-solid fa-people-group" class="fa-2x "/>
      </NuxtLink>
      </li>

    </ul>
  </footer>
</template>

<script setup></script>

<style scoped></style>
