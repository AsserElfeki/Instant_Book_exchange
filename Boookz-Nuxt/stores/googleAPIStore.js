import { defineStore } from 'pinia';

export const useGoogleAPIStore = defineStore({
  id: 'googleAPIStore',
  state: () => ({
    books: [],
  }),
  actions: {
    async searchForBook(bookTitle) {
      //Todo : change link
      const data = await $fetch(
        'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle
      );
      this.books = data;
      console.log(this.books);
    },
  },
  getters: {},
});
