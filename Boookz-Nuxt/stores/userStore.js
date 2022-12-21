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
                    await navigateTo('/profile')

                }
            }
            catch (error) {
                console.log(error);
            }

        },

        async register(form) {
            try {
                const res = await $fetch('http://localhost:8000/authentication/register/', {
                    method: 'POST',
                    body: form
                })
                if (res.response) {
                    //display a toast that says register successful 
                }
                else {
                    if (res.username) {
                        //display a toast that says username already exists
                    }
                    else if (res.email) {
                        //display a toast that says email already exists
                    }
                    else if (res.password) {
                        //display a toast that says password is too short
                    }
                    else if (res.password2) {
                        //display a toast that says passwords do not match
                    }
                }
            }
            catch (error) {
                console.log(error);
            }

        },

        async logOut() {
            const res = await $fetch('http://localhost:8000/authentication/logout_all/', {
                method: 'POST',
                headers: { "authorization": "Bearer " + this.token }
            })
            this.userIsLoggedIn = false;
            this.token = '';
        }
    },

    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        storage: persistedState.sessionStorage,
    },

});
