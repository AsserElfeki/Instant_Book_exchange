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
      const res = await $fetch('http://146.59.87.108:8000/data/wanted/');
      this.wantedBooks = res;
    },

    async getOfferedBooksFromDB() {
      const res = await $fetch('http://146.59.87.108:8000/data/giveaway/');
      this.giveAwayBooks = res;
      this.randomBook = this.giveAwayBooks[Math.floor(Math.random() * this.giveAwayBooks.length)];
    },
    setClickedBook(book) {
      this.clickedBook = book;
      this.persist
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


