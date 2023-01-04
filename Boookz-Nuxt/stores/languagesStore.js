import { defineStore } from 'pinia';
import ISO6391 from 'iso-639-1';

export const useLangAPIStore = defineStore({
    id: 'langAPIStore',
    state: () => ({
        languages: [],
        chosenLangName: '',
        chosenLangCode: '',
    }),
    actions: {
        getAllLanguages() {
            this.languages = ISO6391.getAllNativeNames()
            return this.languages
        },

        getLanguageCode(language) {
            return ISO6391.getCode(language)
        },

        getlanguageEnglishName(language) {
            return ISO6391.getName(language)
        },
        
        chooseLanguage(lang) {
            this.chosenLangName = lang;
            this.chosenLangCode = this.getLanguageCode(lang)
        }
    },
    getters: {},
});
