import { defineStore } from 'pinia';
export const useUserStore = defineStore({
    id: 'userStore',
    state: () => ({
        userName: '',
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
        chosenBookForATrade: {},
        registerSuccess: false,
        addBookSuccessfull: false,
        BE_API: "https://boookzexchange.store:4433/"
    }),
    actions: {
        async signIn(form) {
            try {
                const res = await $fetch(this.BE_API+'authentication/login/', {
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
                const res = await $fetch(this.BE_API+'authentication/register/', {
                    method: 'POST',
                    body: form
                })
                this.registerSuccess = true;
            }
            catch (error) {
                this.registerError = error.data;
                this.registerSuccess = false;
            }
        },

        async logOut() {
            await $fetch(this.BE_API+'authentication/logout_all/', {
                method: 'POST',
                headers: { "authorization": "Bearer " + this.token }
            })
            // this.userIsLoggedIn = false;
            // this.token = '';
            this.$reset();
            await navigateTo('/')
        },
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
                const res = await $fetch(this.BE_API+'authentication/profile/', {
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
                const res = await $fetch(this.BE_API+'data/upload/' + shelf, {
                    method: 'POST',
                    headers: {
                        "authorization": "Bearer " + this.token,
                    },
                    body: form
                })
                if (res.success) {
                    this.addBookSuccessfull = true;
                    await this.getUserInfo();
                }
            }
            catch (error) {
                this.addBookError = error.data;
                this.addBookSuccessfull = false;
            }
        },

        async deleteBook(book) {
            const res = await $fetch(this.BE_API+'data/delete/' + book.pk, {
                method: 'DELETE',
                headers: {
                    "authorization": "Bearer " + this.token,
                },
            })
            await this.getUserInfo();
        },

        async startTransaction(initiator_book, receiver_book) {
            const res = await $fetch(this.BE_API+'transaction/startTransaction/', {
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
        },

        async deleteNotification(pk) {
            const res = await $fetch(this.BE_API+'authentication/notification_delete/' + pk, {
                method: 'DELETE',
                headers: {
                    "authorization": "Bearer " + this.token,
                }
            })
            await this.getUserInfo();
        },

        async acceptTransaction(pk) {
            const res = await $fetch(this.BE_API+'transaction/confirm/' + pk, {
                method: 'PUT',
                headers: {
                    "authorization": "Bearer " + this.token,
                }
            })
            await this.getUserInfo();
        },

        async declineTransaction(pk) {
            const res = await $fetch(this.BE_API+'transaction/decline/' + pk, {
                method: 'PUT',
                headers: {
                    "authorization": "Bearer " + this.token,
                }
            })
            await this.getUserInfo();
        },

        async confirmBookRecieved(pk) {
            const res = await $fetch(this.BE_API+'transaction/confirmReceive/' + pk, {
                method: 'PUT',
                headers: {
                    "authorization": "Bearer " + this.token,
                }
            })
            await this.getUserInfo();
        },

        async rateTransaction(pk, form) {
            const res = await $fetch(this.BE_API+'transaction/rate/' + pk, {
                method: 'POST',
                headers: {
                    "authorization": "Bearer " + this.token,
                },
                body: form
            })
            await this.getUserInfo();
        },

        async sendToSupport(message) {
            await $fetch(this.BE_API+'data/report/', {
                method: 'POST',
                headers: { "authorization": "Bearer " + this.token, },
                body: { "message": message }

            })
        },

        async clearNotifications() {
            await $fetch(this.BE_API +'authentication/notification_delete_all/', {
                method: 'DELETE',
                headers: { "authorization": "Bearer " + this.token, },
            })
            await this.getUserInfo();

        }

    },

    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        storage: persistedState.sessionStorage,
    },

});

