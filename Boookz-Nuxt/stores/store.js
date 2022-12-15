import { defineStore } from 'pinia';

export const useStore = defineStore({
  id: 'store',
  state: () => ({
    books: [],
    userIsSearching: false,
    userIsLoggedIn: false,
  }),
  actions: {
    async retrieveBook() {
      //Todo : change link
      const data = await $fetch('http://localhost:4000/books');
      this.books = data;
      console.log(this.books);
    },
  },

  
  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {

  },
});

// ToDo user and token in data ?

