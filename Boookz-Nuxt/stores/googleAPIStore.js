import { defineStore } from 'pinia';

export const useGoogleAPIStore = defineStore({
    id: 'googleAPIStore',
    state: () => ({
        book_titles: [],
        book_authors: [],
        book_limit: 10,
    }),
    actions: {
        async searchForBookTitles(bookTitle, languageCode) {
            const data = await $fetch(
                'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle + '&maxResults=' + this.book_limit +
                "&langRestrict=" + languageCode
            );
            this.book_titles = [];
            for (const index in data["items"]) {
                this.book_titles.push(data["items"].at(index).volumeInfo.title);
            }
        },
        async getBookAuthorsFromTitle(bookTitle, languageCode) {
            const data = await $fetch(
                'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle +
                '&maxResults=1&projection=lite&langRestrict=' + languageCode
            );
            this.book_authors = data["items"].at(0).volumeInfo.authors
        },
    },
    getters: {},
});

//ToDo: 
// 1. set language of search in google api  - SOLUTION:  langRestrict
// 2. set max results in google api