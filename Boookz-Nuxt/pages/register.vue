<template>
  <div
    class="flex flex-col md:flex-row md:mt-32 mx-auto justify-around items-center gap-1"
  >
    <div class="img">
      <img
        src="../assets/img/register-img.png"
        alt="photo of a lady looking from her window"
      />
    </div>

    <div class="">
      <form
        @submit.prevent="register"
        @input="store.resetErrors"
        class="flex flex-col justify-between gap-3"
      >
        <h1 class="text-3xl font-black">Register</h1>

        <div class="">
          <label for="firstname"></label>
          <input
            required
            class="input"
            size="28"
            type="name"
            name="firstname"
            id="firstname"
            placeholder="first name"
            v-model="form.first_name"
          />
        </div>

        <div class="">
          <label for="lastname"></label>
          <input
            required
            class="input"
            size="28"
            type="name"
            name="lastname"
            id="lastname"
            placeholder="last name"
            v-model="form.last_name"
          />
        </div>

        <div class="">
          <label for="country"></label>
          <input
            required
            class="input"
            size="28"
            type="name"
            name="lastname"
            id="country"
            placeholder="country"
            v-model="form.country"
          />
        </div>

        <div class="">
          <label for="username"></label>
          <input
            required
            class="input"
            size="28"
            type="name"
            name="username"
            id="username"
            placeholder="username"
            v-model="form.username"
          />
          <p
            v-if="store.registerError.username"
            v-for="error in store.registerError.username"
            class="error-message"
          >
            {{ error }}
          </p>
        </div>

        <div class="">
          <label for="email"></label>
          <input
            required
            class="input"
            size="28"
            type="email"
            name="email"
            id="email"
            placeholder="email address"
            v-model="form.email"
          />
          <p
            v-if="store.registerError.email"
            v-for="error in store.registerError.email"
            class="error-message"
          >
            {{ error }}
          </p>
        </div>

        <div class="">
          <label for="password"></label>
          <input
            required
            class="input"
            size="28"
            type="password"
            placeholder="password"
            v-model="form.password"
          />
          <p>{{ form.password }}</p>
          <p
            v-if="store.registerError.password"
            v-for="error in store.registerError.password"
            class="error-message"
          >
            {{ error }}
          </p>
        </div>

        <div class="">
          <label for="password2"></label>
          <input
            required
            class="input"
            size="28"
            type="password"
            placeholder="repeat password"
            v-model="form.password2"
          />
          <p
            v-if="store.registerError.password2"
            v-for="error in store.registerError.password2"
            class="error-message"
          >
            {{ error }}
          </p>
        </div>

        <div class="">
          <input
            type="checkbox"
            name="remember"
            id="remember"
            v-model="form.remember"
          />
          <label for="remember"> Remember me</label>
        </div>
        <div class="btn self-center">
          <button type="submit">Register</button>
        </div>
        <div></div>
      </form>
    </div>
  </div>
</template>

<script setup>
  import { useUserStore } from '~/stores/userStore';
  //data
  const store = useUserStore();
  const remember = ref(false);
  const form = reactive({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    password2: '',
    country: '',
  });

  const {$toast} = useNuxtApp();

  //functions
  async function register() {
    store.resetErrors();
    await store.register(form);
    if (store.registerSuccess) {
      $toast.success('Registration successful', {
        timeout: 3000,
      });
      await navigateTo('/signin');
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
