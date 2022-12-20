import { defineStore } from 'pinia';
export const useUserStore = defineStore({
    id: 'userStore',
    state: () => ({
        userName: '',
        userPassword: '',
        userIsSearching: false,
        userIsLoggedIn: false,
        userWantedBooks: [],
        userGiveAwayBooks: [],
        token: '',

    }),
    actions: {
        async signIn(form) {
            try {
                const res = await $fetch('http://localhost:8000/authentication/login/', {
                    method: 'POST',
                    body: form
                })
                console.log(res.access);
                this.token = res.access;
                if (this.token) {
                    this.userIsLoggedIn = true;
                }
            }
            catch (error) {
                console.log(error);
            }

        },

        async register(form) {
            try {
                return await $fetch('http://localhost:4000/users', {
                    method: 'POST',
                    body: form
                })
            }
            catch (error) {
                console.log(error);
            }

        },

        logOut() {
            this.userIsLoggedIn = false;
            this.token = '';
        }
    },

    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        storage: persistedState.localStorage,
    },

});
