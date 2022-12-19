import { defineStore } from 'pinia';

export const useStore = defineStore({
  id: 'store',
  state: () => ({
    books: [],
    userName: '',
    userPassword: '',
    userIsSearching: false,
    userIsLoggedIn: true,
    wantedBooke: [],
    giveAwayBooks: [],
    userWantedBooks: [],
    userGiveAwayBooks: [],
    randomBook: {},
    token: '',
  }),
  actions: {
    async getBooksFromDB() {
      const res = await $fetch('http://localhost:4000/books');
      this.books = res;
      this.randomBook = this.books[Math.floor(Math.random() * this.books.length)];
      // console.log("books:" + this.books.at(1).title);
    },

    async signIn(form) {
      try {
        const res = $fetch('http://localhost:4000/users', {
          headers: { 'Content-Type': 'application/json' },
          method: 'POST',
          body: form
        })
        this.token = res.access
        if (this.token) {
          this.userIsLoggedIn = true;
        }
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
    // randomBook() {
    //   return this.books[Math.floor(Math.random() * this.books.length)];
    // }
  },
});


