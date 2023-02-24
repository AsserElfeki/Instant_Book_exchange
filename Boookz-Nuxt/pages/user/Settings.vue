<template>
  <div class="flex justify-center container mx-auto gap-4">

    <form @submit.prevent="updateAvatar"
    class="flex flex-col justify-center items-center gap-4 self-start px-2">
      <h2 class="font-sans font-extrabold text-xl self-start my-2">Public Profile</h2>

      <div class="flex flex-row justify-around gap-12 md:w-full">
        <img
          src="../../assets/img/avatar.png"
          alt="avatar"
          class="w-32 h-32 rounded-full object-cover border-4 border-violet-500"
        />
        <div class="flex flex-col gap-4">
          <button type="button" class="btn-dark" @click="changePicture">
            Change Picture
          </button>
          <button type="button" class="btn-light" @click="removePicture">Remove Picture</button>
        </div>
      </div>
    </form>
<div>
    <form @submit.prevent="updateData" class="">
    <h2 class="font-sans font-extrabold text-xl self-start my-2">Personal data</h2>
    <div class="flex flex-col w-full sm:flex-row justify-between gap-4">
        <div class="flex flex-col">
          <label for="name">name</label>
          <input
            id="name"
            type="text"
            v-model="userForm.name"
            class="border-2 border-black p-2 rounded-lg"
          />
        </div>
        <div class="flex flex-col">
          <label for="surname">surname</label>
          <input
            id="surname"
            type="surname"
            v-model="userForm.surname"
            class="border-2 border-black p-2 rounded-lg"
          />
        </div>
      </div>

      <div class="w-full flex flex-col">
        <label class="flex-auto" for="country">country:</label>
        <input
          id="country"
          type="country"
          v-model="userForm.country"
          class="border-2 border-black p-2 rounded-lg flex-auto"
        />
      </div>
    </form>

    <form @submit.prevent="updatePrivacy" class="w-full flex flex-col gap-4 mt-8">
      <h2 class="font-sans font-extrabold text-xl">Privacy</h2>
        <div class="w-full flex flex-col">
          <label for="password">Old password</label>
          <input
            id="password"
            type="password"
            v-model="userForm.password"
            class="border-2 border-black p-2 rounded-lg"
          />
        </div>

        <div class="w-full flex flex-col">
          <label for="newPassword">New password</label>
          <input
            id="newPassword"
            type="password"
            v-model="userForm.newPassword"
            class="border-2 border-black p-2 rounded-lg"
          />
        </div>
        <div class="w-full flex flex-col">
          <label for="passwordConfirm">Confirm password</label>
          <input
            id="passwordConfirm"
            type="password"
            v-model="userForm.passwordConfirm"
            class="border-2 border-black p-2 rounded-lg"
          />
        </div>
    </form>

    <form
      @submit.prevent="updateUser"
      class="flex flex-col justify-center items-center gap-4  px-2"
    >

      <!-- <div class="w-full flex flex-col">
        <label for="Genre">Genre:</label>
        <input
          id="Genre"
          type="Genre"
          v-model="userForm.Genre"
          class="border-2 border-black p-2 rounded-lg"
        />
      </div> -->

      <div class="w-full flex flex-col gap-4 mt-8">
        
      </div>

      <button type="submit" class="btn-dark w-full">SAVE</button>
    </form>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "~/stores/userStore";
const {$toast} = useNuxtApp();

const userStore = useUserStore();

const userForm = reactive({
  name: "",
  surname: "",
  password: "",
  passwordConfirm: "",
});

function updateUser() {
  console.log(userForm);
}
function removePicture() {
  console.log("remove picture");
}

function changePicture() {
  console.log("change picture");
}
// await userStore.getUserData();
</script>

<style lang="scss" scoped>
input {
  border: 2px solid black;
  border-radius: 7px;
  padding: 10px;
}
</style>

//add email 
// split forms 
// add validation
