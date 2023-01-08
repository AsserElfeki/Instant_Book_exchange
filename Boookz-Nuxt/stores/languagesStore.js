import { defineStore } from 'pinia';
import ISO6391 from 'iso-639-1';

export const useLangAPIStore = defineStore({
    id: 'langAPIStore',
    state: () => ({
        languages: [],
        chosenLangNativeName: '',
        chosenLangCode: '',
        chosenLangEnglishName: ''
    }),
    actions: {

        getAllLanguages() {
            this.languages = ISO6391.getAllNames()
            return this.languages
        },

        chooseLanguage(lang) {
            this.chosenLangNativeName = lang;
            this.chosenLangCode = ISO6391.getCode(lang)
            this.chosenLangEnglishName = ISO6391.getName(this.chosenLangCode)
        }
    },
    getters: {},
});
