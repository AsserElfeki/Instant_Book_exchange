import { defineStore } from 'pinia';
export const useUserStore = defineStore({
    id: 'userStore',
    state: () => ({
        userName: 'Leonardo Davinci',
        userPassword: '',
        userProfileImage: "",
        userIsSearching: false,
        userIsLoggedIn: false,
        userWantedBooks: [],
        userGiveAwayBooks: [],
        region: '',
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
            try {
                const res = await $fetch('http://146.59.87.108:8000/authentication/profile/', {
                    headers: {
                        "authorization": "Bearer " + this.token,
                    }
                })

                if (res) {
                    //console.log("name: ", res.at(0))
                    this.userName = res.at(0).username;
                    this.userIsLoggedIn = true;
                    if (res.at(0).book_reader.giveaway_books[0]) {
                        this.userGiveAwayBooks = res.at(0).book_reader.giveaway_books
                    }
                    if (res.at(0).book_reader.wanted_books[0]) {
                        this.userWantedBooks = res.at(0).book_reader.wanted_books
                    }
                    this.region = res.at(0).book_reader.country;
                    this.userProfileImage = res.at(0).book_reader.profile_image;
                    // this.userRatings = res.book_reader.ratings
                    // this.userTransactions = res.book_reader.history
                }

            }
            catch (error) {
                console.log("login error " + JSON.stringify(error.data));
            }

            //ToDO
        },

        async addBook(form, shelf) {
            const res = await $fetch('http://146.59.87.108:8000/data/upload/' + shelf, {
                method: 'POST',
                headers: {
                    "authorization": "Bearer " + this.token,
                },
                body: form
            })
            await this.getUserInfo();
        }
    },



    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        // storage: persistedState.sessionStorage,
    },

});

