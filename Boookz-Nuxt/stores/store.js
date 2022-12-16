import { defineStore } from 'pinia';

export const useStore = defineStore({
  id: 'store',
  state: () => ({
    books: [],
    userName: '',
    userPassword: '',
    userIsSearching: false,
    userIsLoggedIn: false,
  }),
  actions: {
    async retrieveBook() {
      //Todo : change link
      const data = await $fetch('http://localhost:4000/books');
      this.books = data;
      // console.log(this.books);
    },
    async signIng(userName, userPassword) {
      this.userIsLoggedIn = true;
      //ToDO 2
    },
  },

  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {},
});

// ToDo :
//1. user and token in data ?
//2. Post request to backend with user name and password
