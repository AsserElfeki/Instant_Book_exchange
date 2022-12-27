import { useUserStore } from '~/stores/userStore'
const store = useUserStore()
const isAuthenticated = store.userIsLoggedIn

console.log(isAuthenticated)
export default defineNuxtRouteMiddleware((to, from) => {
    // isAuthenticated() is an example method verifying if an user is authenticated
    console.log(isAuthenticated)
    if (isAuthenticated === false) {
        return navigateTo('signIn')
    }
})
