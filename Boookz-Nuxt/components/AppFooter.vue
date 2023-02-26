<template>
  <footer class="mt-8 bg-violet-400">
    <ul
      class="footer max-w-screen-xl flex justify-between items-center mx-auto py-2"
    >
      <li
        class="hover:text-white border-b-2 border-transparent hover:border-white"
      >
        <a
          href="https://github.com/AsserElfeki/Instant_Book_exchange"
          target="_blank"
          class="flex flex-col-reverse"
        >
          <p class="text-center">GitHub Repo</p>
          <font-awesome-icon
            icon="fa-brands fa-github"
            class="fa-2x"
          />
        </a>
      </li>

      <li
        class="hover:text-white border-b-2 border-transparent hover:border-white"
      >
        <a
          href="https://www.linkedin.com/in/asserelfeki/"
          target="_blank"
          class="flex flex-col-reverse"
        >
          <p class="text-center">LinkedIn</p>
          <font-awesome-icon
            icon="fa-brands fa-linkedin"
            class="fa-2x"
          />
        </a>
      </li>

      <li
        class="hover:text-white border-b-2 border-transparent hover:border-white"
      >
        <NuxtLink
          to=""
          class="flex flex-col-reverse justify-center items-center"
        >
          <p class="text-center">About</p>
          <font-awesome-icon
            icon="fa-solid fa-people-group"
            class="fa-2x"
          />
        </NuxtLink>
      </li>

      <li
        class="hover:text-white border-b-2 border-transparent hover:border-white"
      >
        <NuxtLink
          to="/support"
          class="flex flex-col-reverse"
        >
          <p class="text-center">Support</p>
          <font-awesome-icon
            icon="fa-solid fa-headset"
            class="fa-2x"
          />
        </NuxtLink>
      </li>
    </ul>
  </footer>
</template>

<script setup></script>

<style scoped></style>
