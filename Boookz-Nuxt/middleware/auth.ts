import { useUserStore } from '~/stores/userStore'
const store = useUserStore()
const isAuthenticated = store.userIsLoggedIn

export default defineNuxtRouteMiddleware(() => {
    // isAuthenticated() is an example method verifying if an user is authenticated
    // console.log("state: " + isAuthenticated)
    // console.log({ to, from })
    if (process.client && isAuthenticated === false) {
        return navigateTo('/signIn')
    }
    
})
