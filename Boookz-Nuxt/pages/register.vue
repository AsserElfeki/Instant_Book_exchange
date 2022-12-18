<template>
    <div class=" flex mt-32 mx-auto  justify-center items-center gap-40 ">
        <div class="img ">
            <img src="../assets/img/register-img.png" alt="photo of a lady looking from her window">
        </div>

        <div class="">
            <form action="" class="flex flex-col justify-between gap-4">
                <h1 class="text-3xl font-black ">Register</h1>
                <div class="">
                    <label for="email"></label>
                    <input class="input" size="28" type="email" name="email" id="email" placeholder="Enter your email"
                        v-model="form.email">
                    <p>username: {{ form.email }}</p>
                </div>

                <div class="">
                    <label for="password"></label>
                    <input class="input" size="28" type="password" placeholder="Enter your password"
                        v-model="form.password">
                    <p>password {{ form.password }}</p>
                </div>

                <div class="">
                    <label for="password"></label>
                    <input class="input" size="28" type="password" placeholder="repeat password" >
                </div>

                <div class="">
                    <input type="checkbox" name="remember" id="remember" v-model="form.remember">
                    <label for="remember"> Remember me</label>
                </div>
                <div class="flex justify-center">
                    <button type="" class="btn" @click="signIn">Register</button>
                </div>

                
            </form>
        </div>
    </div>
</template>

<script setup>
import { v4 as uuidv4 } from "uuid"
import { useStore } from '~/stores/store'

//data 
const store = useStore()
const remember = ref(false)
const id = uuidv4()
const form = reactive({
    id: id,
    email: '',
    password: '',
    remember: remember
})

//functions
async function signIn() {
    store.signIn(form)
}
</script>

<style scoped>
.input {
    border: 2px solid black;
    border-radius: 7px;
    padding: 10px;
}
</style>