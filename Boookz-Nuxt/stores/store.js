import { defineStore } from 'pinia';

export const useStore = defineStore({
  id: 'store',
  state: () => ({
    books: [],
    userName: '',
    userPassword: '',
    userIsSearching: false,
    userIsLoggedIn: true,
  }),
  actions: {
    async getBooksFromDB() {
      //Todo 1
      const res = await $fetch('http://localhost:4000/books');
      // const data = await res.json();
      this.books = res;
      // console.log(this.books);
    },

    async signIn(form) {
      try {
        return await $fetch('http://localhost:4000/users', {
          headers: { 'Content-Type': 'application/json' },
          method: 'POST',
          body: form
        })
      } catch (error) {
        console.log(error);
      }

    },

    async register(form) {
      try {
        return await $fetch('http://localhost:4000/users', {
          headers: { 'Content-Type': 'application/json' },
          method: 'POST',
          body: form
        })
      } catch (error) {
        console.log(error);
      }

    },
  },

  //to get specific parts of data, like select <items> from <container> WHERE <condition>
  getters: {

  },
});


