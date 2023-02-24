import { defineStore } from 'pinia';
export const useProfileStore = defineStore({
    id: 'profileStore',
    state: () => ({
        userName: 'Leonardo Davinci',
        userProfileImage: "",
        userWantedBooks: [],
        userGiveAwayBooks: [],
        region: '',
        userTransactions: [],
        userRatings: [],
        BE_API: "https://boookzexchange.store:4433/"
    }),
    actions: {
        async getUserInfo() {
            try {
                const res = await $fetch(this.BE_API + 'authentication/profile/' + this.userName, {
                })
                if (res) {
                    if (res.book_reader.giveaway_books[0]) {
                        this.userGiveAwayBooks = res.book_reader.giveaway_books
                    }
                    if (res.book_reader.wanted_books[0]) {
                        this.userWantedBooks = res.book_reader.wanted_books
                    }
                    this.region = res.book_reader.country;
                    this.userProfileImage = res.book_reader.profile_image;
                    this.userRatings = res.book_reader.ratings
                    this.userTransactions = res.book_reader.transactions
                }

            }
            catch (error) {
                console.log("login error " + JSON.stringify(error.data));
            }

        },
    },
    //to get specific parts of data, like select <items> from <container> WHERE <condition>
    getters: {
    },
    persist: {
        // storage: persistedState.sessionStorage,
    },

});

