import {defineStore} from 'pinia';

export const useGoogleAPIStore = defineStore({
    id: 'googleAPIStore',
    state: () => ({
        book_titles: [],
        book_image: null,
        book_limit: 5,
    }),
    actions: {
        async searchForBookTitles(bookTitle, languageCode) {
            const data = await $fetch(
                'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle + '&maxResults=' + this.book_limit +
                "&projection=lite&langRestrict=" + languageCode
            );
            this.book_titles = [];
            for (const index in data["items"]) {
                this.book_titles.push(data["items"].at(index).volumeInfo.title);
            }
        },
        async getBookThumbnailFromTitle(bookTitle, languageCode) {
            const data = await $fetch(
                'https://www.googleapis.com/books/v1/volumes?q=' + bookTitle +
                '&maxResults=1&projection=lite&langRestrict=' + languageCode
            );
            this.book_image = data["items"].at(0).volumeInfo.imageLinks.thumbnail
        },
    },
    getters: {},
});

//ToDo: 
// 1. set language of search in google api  - SOLUTION:  langRestrict
// 2. set max results in google api