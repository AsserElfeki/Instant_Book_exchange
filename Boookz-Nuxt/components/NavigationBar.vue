<template>

    <div class="navBar">
        <NuxtLink to="/" class="flex gap-2 justify-start self-start">
            <AppLogo />
            <div class="app-name gap-8">
                <h1 class="hi">Boookz</h1>
                <p class="text-xs">Book xchange website</p>
            </div>
        </NuxtLink>
        <div class="search-box">
            <input placeholder="Search" type="text" class="search-bar" v-model="searchQuery">
            <button class="" @click="search">
                <img src="/MagnifyingGlass.png" alt="search icon" class="absolute top-0 right-2 ">
            </button>
        </div>
        <ul class="flex flex-row gap-6 lg:gap-2 ">
            <NuxtLink class="btn" to="/signin" v-if="!store.userIsLoggedIn">Sign in</NuxtLink>
            <NuxtLink class="btn" to="/register" v-if="!store.userIsLoggedIn">Sign up</NuxtLink>
            <NuxtLink class="btn" to="/profile" v-if="store.userIsLoggedIn">Profile</NuxtLink>
            <NuxtLink to="/signIn" v-if="store.userIsLoggedIn" @click="logOut" class="btn">Log Out</NuxtLink>
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
.appname h1 {
    font-size: 3.5rem;
    font-weight: 100;
}

.hi {
    width: 117px;
    height: 35px;
    font-family: 'Segoe UI';
    font-style: normal;
    font-weight: 700;
    font-size: 33px;
    line-height: 44px;
}
</style>


