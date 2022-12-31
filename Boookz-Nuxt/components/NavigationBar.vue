<template>

    <div class="flex flex-col gap-3 mx-5 my-9 justify-between items-center lg:flex-row">
        <NuxtLink to="/" class="flex gap-2 justify-start self-start">
            <AppLogo />
            <div class="gap-8">
                <h1 class="hi font-bold text-[33px] leading-10 h-9 font-segoe">Boookz</h1>
                <p class="text-xs">Book xchange website</p>
            </div>
        </NuxtLink>
        <div class="flex my-auto items-center relative">
            <input placeholder="Search" type="text" class="bg-gray-100 rounded-lg px-3 w-60 md:w-96 h-8"
                v-model="searchQuery">
            <button class="" @click="search">
                <img src="/MagnifyingGlass.png" alt="search icon" class="absolute top-0 right-2 ">
            </button>
        </div>
        <ul class="flex flex-row gap-6 lg:gap-2 ">
            <NuxtLink class="btn-sm lg:btn" to="/signin" v-if="!store.userIsLoggedIn">Sign in</NuxtLink>
            <NuxtLink class="btn-sm lg:btn" to="/register" v-if="!store.userIsLoggedIn">Sign up</NuxtLink>
            <NuxtLink class="btn-sm lg:btn" to="/profile" v-if="store.userIsLoggedIn">Profile</NuxtLink>
            <NuxtLink class="btn-sm lg:btn" to="/signin" v-if="store.userIsLoggedIn" @click="logOut">Log Out</NuxtLink>
        </ul>
    </div>

</template>

<script>
import { useGoogleAPIStore } from '~/stores/googleAPIStore';
import { useUserStore } from '~/stores/userStore';

//here I am using the setup function explicitly, but you can also use the composition API
//if you need to access so state, remember to add it to the return object
//I Love github copilot <3 
export default {
    setup() {
        const googleAPIStore = useGoogleAPIStore()
        const store = useUserStore()

        const searchQuery = ref('')
        // const userIsLoggedIn = store.userIsLoggedIn

        const search = () => {
            googleAPIStore.searchForBook(searchQuery.value)
        }

        const logOut = () => {
            store.logOut()

        }
        return { searchQuery, googleAPIStore, search, store, logOut }
    }
}

</script>

<style scoped>
.hi {

    font-family: 'Segoe';

}
</style>


