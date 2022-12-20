import { defineStore } from 'pinia';

export const useDataStore = defineStore({
  id: 'dataStore',
  state: () => ({
    books: [],
    wantedBooks: [],
    giveAwayBooks: [],
    randomBook: {},
  }),
  actions: {
    async getBooksFromDB() {
      const res = await $fetch('http://localhost:4000/books');
      this.books = res;
      this.randomBook = this.books[Math.floor(Math.random() * this.books.length)];
      // console.log("books:" + this.books.at(1).title);
    },

  },

  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {

  },

  persist: {
    storage: persistedState.localStorage,
  },
});


