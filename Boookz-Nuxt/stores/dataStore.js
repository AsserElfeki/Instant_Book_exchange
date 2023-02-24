import { defineStore } from 'pinia';
import { navigateTo } from "nuxt/app";
import { useUserStore } from './userStore';

export const useDataStore = defineStore({
  id: 'dataStore',
  state: () => ({
    wantedBooks: [],
    giveAwayBooks: [],
    randomBook: {},
    clickedBook: {},
    searchResults: [],
    BE_API: "https://boookzexchange.store:4433/",
  }),
  actions: {
    async getWantedBooksFromDB() {
      const res = await $fetch(this.BE_API + 'data/wanted/');
      const userStore = useUserStore();
      if (userStore.userIsLoggedIn) {
        const booksInArea = res.filter(item => {
          return (item.book_owner.country === userStore.region && item.book_owner.username !== userStore.userName)
        })
        this.wantedBooks = booksInArea;
      }
      else {
        this.wantedBooks = res;
      }
    },

    async getOfferedBooksFromDB() {
      const res = await $fetch(this.BE_API + 'data/giveaway/');
      const userStore = useUserStore();
      if (userStore.userIsLoggedIn) {
        const booksInArea = res.filter(item => {
          return (item.book_owner.country === userStore.region && item.book_owner.username !== userStore.userName)
        })
        this.giveAwayBooks = booksInArea;
      }
      else {
        this.giveAwayBooks = res;
      }
      this.randomBook = this.giveAwayBooks[Math.floor(Math.random(1) * this.giveAwayBooks.length)];
    },
    setClickedBook(book) {
      this.clickedBook = book;
      this.persist
    },

    async searchForBook(book_title) {
      const res = await $fetch(this.BE_API + 'data/search?search=' + book_title);
      this.searchResults = res;
      await navigateTo("/SearchResults")
    },


    async updateData() {
      await this.getWantedBooksFromDB();
      await this.getOfferedBooksFromDB();
    }

  },

  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {

  },

  persist: {
    enabled: true,
    storage: persistedState.localStorage,
  },
});


