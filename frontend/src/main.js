import { createApp } from 'vue'
import App from './App.vue'
import router from './router' 
import axios from 'axios'
import Vue from 'vue'

// set a prototype for http
Vue.prototype.$http = axios;

createApp(App).use(router).mount('#app')
