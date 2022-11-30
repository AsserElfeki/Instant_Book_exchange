import { createApp } from 'vue'
import App from './App.vue'
import router from './router' 


// set a prototype for http

createApp(App).use(router).mount('#app')
