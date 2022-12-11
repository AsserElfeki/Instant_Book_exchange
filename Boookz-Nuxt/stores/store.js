// store/filters.js
import { defineStore } from 'pinia'

export const useStore = defineStore({
  id: 'store',
  state: () => ({
      books: [],
  }),
  actions: {
    async retrieveBook() {
      //Todo : change link
      const data = await $fetch('http://localhost:4000/books')
      this.books = data
      console.log(this.books)
    }
  },
  getters: {
   
  },
})


// ToDo user and token in data ? 