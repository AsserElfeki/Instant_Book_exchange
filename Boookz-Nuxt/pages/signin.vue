<template>

  <div class=" flex mt-32 mx-auto  justify-center items-center gap-40 ">
    <div class="img ">
      <img src="../assets/img/sign-in-img.png" alt="photo of a lady looking from her window">
    </div>

    <div class="">
      <div action="" class="flex flex-col justify-between gap-4">
        <h1 class="text-3xl font-black ">Sign in</h1>
        <div class="">
          <label for="email"></label>
          <input class="input" size="28" type="email" name="email" id="email" placeholder="Enter your email"
            v-model="email">
          <p>username: {{ email }}</p>
        </div>

        <div class="">
          <label for="password"></label>
          <input class="input" size="28" type="password" placeholder="Enter your password" v-model="password">
          <p>password {{ password }}</p>
        </div>

        <div class="">
          <input type="checkbox" name="remember" id="remember">
          <label for="remember"> Remember me</label>
        </div>
        <div class="">
          <button type="" class="btn" @click="signIn">Sign in</button>
        </div>

        <div
          class="text-blue-300 border border-transparent rounder hover:border hover:rounded hover:shadow-md mx-auto px-2 ">
          <p>
            <NuxtLink to="/register">Don't have an account? Sign up</NuxtLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from '~/stores/store'
const store = useStore()

const email = ref('')
const password = ref('')

const signIn = () => {
  store.signIn(email.value, password.value)
}

</script>

<style scoped>
.input {
  border: 2px solid black;
  border-radius: 7px;
  padding: 10px;
}
</style>
