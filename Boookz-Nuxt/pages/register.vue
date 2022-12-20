<template>
    <div class="flex mt-32 mx-auto justify-around items-center gap-1">
        <div class="img">
            <img src="../assets/img/register-img.png" alt="photo of a lady looking from her window" />
        </div>

        <div class="">
            <form @submit.prevent="register" class="flex flex-col justify-between gap-3">
                <h1 class="text-3xl font-black">Register</h1>

                <div class="">
                    <label for="firstname"></label>
                    <input required class="input" size="28" type="name" name="firstname" id="firstname"
                        placeholder="first name" v-model="form.firstname" />
                </div>

                <div class="">
                    <label for="lastname"></label>
                    <input required class="input" size="28" type="name" name="lastname" id="lastname"
                        placeholder="last name" v-model="form.lastname" />
                </div>

                <div class="">
                    <label for="username"></label>
                    <input required class="input" size="28" type="name" name="username" id="username"
                        placeholder="username" v-model="form.username" />
                    <p>username: {{ form.username }}</p>
                </div>

                <div class="">
                    <label for="email"></label>
                    <input required class="input" size="28" type="email" name="email" id="email"
                        placeholder="email address" v-model="form.email" />
                    <p>{{ form.email }}</p>
                </div>

                <div class="">
                    <label for="password"></label>
                    <input required class="input" size="28" type="password" placeholder="password"
                        v-model="form.password" />
                    <p>password {{ form.password }}</p>
                </div>

                <div class="">
                    <label for="password2"></label>
                    <input required class="input" size="28" type="password" placeholder="repeat password"
                        v-model="form.password2" />
                </div>

                <div class="">
                    <input type="checkbox" name="remember" id="remember" v-model="form.remember" />
                    <label for="remember"> Remember me</label>
                </div>
                <div class="flex justify-center">
                    <button type="submit" class="btn">Register</button>
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
const id = uuidv4();
const form = reactive({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password2: "",
});

//functions
async function register() {
    store.register(form);
}
</script>

<style scoped>
.input {
    border: 2px solid black;
    border-radius: 7px;
    padding: 10px;
}
</style>
