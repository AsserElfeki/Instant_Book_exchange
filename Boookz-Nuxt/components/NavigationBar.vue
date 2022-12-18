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
            <NuxtLink class="btn" to="/signin">Sign in</NuxtLink>
            <NuxtLink class="btn" to="/register">Sign up</NuxtLink>
            <NuxtLink class="btn" to="/profile">Profile</NuxtLink>
        </ul>
    </div>

</template>

<script>
import { useGoogleAPIStore } from '~/stores/googleAPIStore';

export default {
    setup() {
        const searchQuery = ref('')
        const googleAPIStore = useGoogleAPIStore()

        const search = () => {
            googleAPIStore.searchForBook(searchQuery.value)
        }

        return { searchQuery, googleAPIStore, search }
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

// ToDO : 
// 1. Add a search bar ✅
// 2. Add a search button ✅
// 3. Add a search function ✅
// 6. Add a search result component to the home page
// 7. get authentication status and display nav bar accordingly

