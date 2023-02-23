<template>
  <div class="flex flex-col md:flex-row md:mt-32 mx-auto justify-around items-center gap-1">
    <div class="img">
      <img
        src="../assets/img/sign-in-img.png"
        alt="photo of a lady looking from her window"
      />
    </div>

    <div class="">
      <form
        @submit.prevent="signIn"
        @input="store.resetErrors"
        class="flex flex-col justify-between gap-4"
      >
        <h1 class="text-3xl font-black">Sign in</h1>
        <div class="">
          <label for="email"></label>
          <input
            class="input"
            size="28"
            type="text"
            name="email"
            id="email"
            placeholder="Enter your username"
            v-model="form.username"
          />
          <p v-if="store.loginError" class="error-message">
            Username or password are invalid
          </p>
        </div>

        <div class="">
          <label for="password"></label>
          <input
            class="input"
            size="28"
            type="password"
            placeholder="Enter your password"
            v-model="form.password"
          />
        </div>

        <div class="">
          <input type="checkbox" name="remember" id="remember" v-model="form.remember" />
          <label for="remember"> Remember me</label>
        </div>
        <div class="btn self-center">
          <button>Sign in</button>
        </div>

        <div
          class="text-blue-300 border border-transparent rounder hover:border hover:rounded hover:shadow-md mx-auto px-2"
        >
          <p>
            <NuxtLink to="/register">Don't have an account? Sign up</NuxtLink>
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { v4 as uuidv4 } from "uuid";
import { useUserStore } from "~/stores/userStore";

//data
const store = useUserStore();
const remember = ref(false);
let id = uuidv4();
const form = reactive({
  id: id,
  username: "",
  password: "",
  remember: remember,
});
const {$toast} = useNuxtApp();

//functions
async function signIn() {
  await store.signIn(form);
  if (store.userIsLoggedIn) {
    $toast.success("You are logged in", {
      timeout: 3000,
      
    });
  }
}
</script>

<style scoped>
.input {
  border: 2px solid black;
  border-radius: 7px;
  padding: 10px;
}
</style>
