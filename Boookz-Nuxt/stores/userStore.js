import { defineStore } from 'pinia';
export const useUserStore = defineStore({
    id: 'userStore',
    state: () => ({
        userName: 'Leonardo Davinci',
        userPassword: '',
        userIsSearching: false,
        userIsLoggedIn: false,
        userWantedBooks: [],
        userGiveAwayBooks: [],
        region: 'Poland',
        userTransactions: [],
        userRatings: [],
        token: '',
        registerError: {
        },
        loginError: "",
        callingComponent: null
    }),
    actions: {
        async signIn(form) {
            try {
                const res = await $fetch('http://146.59.87.108:8000/authentication/login/', {
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
                console.log("login error" + JSON.stringify(error.data));
                this.loginError = error.data;
            }

        },

        async register(form) {
            try {
                const res = await $fetch('http://146.59.87.108:8000/authentication/register/', {
                    method: 'POST',
                    body: form
                })
                console.log(res);
                if (res.response) {
                }
            }
            catch (error) {
                console.log("error: " + JSON.stringify(error.data));
                this.registerError = error.data;
            }

        },

        async logOut() {
            const res = await $fetch('http://146.59.87.108:8000/authentication/logout_all/', {
                method: 'POST',
                headers: { "authorization": "Bearer " + this.token }
            })
            // this.userIsLoggedIn = false;
            // this.token = '';
            this.$reset();
        },

        // async getUserWantedBooks() {
        //     const res = await $fetch('http://146.59.87.108:8000/data/shelf/wanted', {
        //         headers: { "authorization": "Bearer " + this.token }
        //     })
        //     this.userWantedBooks = res;
        // },

        // async getUserGiveAwayBooks() {
        //     const res = await $fetch('http://146.59.87.108:8000/data/shelf/giveaway', {
        //         headers: { "authorization": "Bearer " + this.token }
        //     })
        //     this.userGiveAwayBooks = res;
        // },
        //ToDo : change endpoints and request maybe 
        // async getUserHistory() {
        //     const res = await $fetch('http://146.59.87.108:8000/data/shelf/giveaway', {
        //         headers: { "authorization": "Bearer " + this.token }
        //     })
        //     this.userTransactions = res;
        // },
        // async getUserRatings() {
        //     const res = await $fetch('http://146.59.87.108:8000/data/shelf/giveaway', {
        //         headers: { "authorization": "Bearer " + this.token }
        //     })
        //     this.userRatings = res;
        // },

        resetErrors() {
            this.registerError = {};
            this.loginError = "";
        },

        getRoute(event) {
            console.log(event.target.value);
            // this.callingComponent=event.target 
        },

        async getUserInfo() {
            const res = await $fetch('http://146.59.87.108:8000/authentication/profile/', {
                headers: { "authorization": "Bearer " + this.token,}
            })
            this.userName = res.username;
            this.region = res.book_reader.country;
            this.userIsLoggedIn = true;
            this.userGiveAwayBooks = res.book_reader.giveaway_shelf.books
            this.userWantedBooks = res.book_reader.wanted_shelf.books
            // this.userRatings = res.book_reader.ratings
            // this.userTransactions = res.book_reader.history

            //ToDO
        },

        async addBook(form) {
            const res = await $fetch('http://146.59.87.108:8000/data/upload/giveaway', {
                method: 'POST',
                headers: {
                    "authorization": "Bearer " + this.token,
                        },
                body: form
            })
        }
    },



    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        // storage: persistedState.sessionStorage,
    },

});

