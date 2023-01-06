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
        callingComponent: null,
        addBookError: {},
        notifications: [],
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
                this.loginError = error.data;
            }

        },

        async register(form) {
            try {
                const res = await $fetch('http://146.59.87.108:8000/authentication/register/', {
                    method: 'POST',
                    body: form
                })
                if (res.response) {
                    //ToDo toast
                }
            }
            catch (error) {
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
                    this.userName = res.username;
                    this.userIsLoggedIn = true;
                    this.userGiveAwayBooks = res.book_reader.giveaway_books
                    this.userWantedBooks = res.book_reader.wanted_books
                    this.region = res.book_reader.country;
                    this.userProfileImage = res.book_reader.profile_image;
                    this.userRatings = res.book_reader.ratings
                    this.userTransactions = res.book_reader.transactions
                    this.notifications = res.book_reader.notifications
                }

            }
            catch (error) {
                console.log("login error " + JSON.stringify(error.data));
            }

            //ToDO
        },

        async addBook(form, shelf) {
            try {
                const res = await $fetch('http://146.59.87.108:8000/data/upload/' + shelf, {
                    method: 'POST',
                    headers: {
                        "authorization": "Bearer " + this.token,
                    },
                    body: form
                })
                if (res.success) {
                    await this.getUserInfo();
                }
            }
            catch (error) {
                this.addBookError = error.data;
            }
        },

        async deleteBook(book) {
            const res = await $fetch('http://146.59.87.108:8000/data/delete/' + book.pk, {
                method: 'DELETE',
                headers: {
                    "authorization": "Bearer " + this.token,
                },
            })
            await this.getUserInfo();
        },

        async startTransaction(initiator_book, receiver_book) {
            const res = await $fetch('http://146.59.87.108:8000/transaction/startTransaction/', {
                method: 'POST',
                headers: {
                    "authorization": "Bearer " + this.token,
                },
                body: {
                    "initiator_book": initiator_book,
                    "receiver_book": receiver_book
                },
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

