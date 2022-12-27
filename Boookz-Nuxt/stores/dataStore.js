import { defineStore } from 'pinia';

export const useDataStore = defineStore({
  id: 'dataStore',
  state: () => ({
    wantedBooks: [],
    giveAwayBooks: [],
    randomBook: {},
    clickedBook: {},
  }),
  actions: {
    async getWantedBooksFromDB() {
      const res = await $fetch('http://127.0.0.1:8000/data/wanted/');
      this.wantedBooks = res;
    },

    async getOfferedBooksFromDB() {
      const res = await $fetch('http://127.0.0.1:8000/data/giveaway/');
      this.giveAwayBooks = res;
      this.randomBook = this.giveAwayBooks[Math.floor(Math.random() * this.giveAwayBooks.length)];
    },
    getClickedBook(book) {
      this.clickedBook = book;
    }
      
  },

  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {

  },

  persist: {
    storage: persistedState.sessionStorage,
  },
});


