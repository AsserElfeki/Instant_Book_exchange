import { defineStore } from 'pinia';

export const useGoogleAPIStore = defineStore({
  id: 'googleAPIStore',
  state: () => ({
    book: [],
  }),
  actions: {
    async searchForBook(bookTitle) {
      //Todo : change link
      const data = await $fetch(
        'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle
      );
      this.book = data;
      console.log(this.book);
    },
  },
  getters: {},
});
