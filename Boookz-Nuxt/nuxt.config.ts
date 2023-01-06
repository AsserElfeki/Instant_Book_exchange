import { MiddlewareKey } from './.nuxt/types/middleware.d';
import vuetify from './plugins/vuetify';


// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },

    head: {
      title: 'BoookZ',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: '' },
        { name: 'format-detection', content: 'telephone=no' },

      ],
      script: [],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Mulish:wght@300&family=Poppins:wght@600&display=swap',
        },
      ],
      // please note that this is an area that is likely to change
      style: [],
      noscript: [
        // <noscript>Javascript is required</noscript>
        { children: 'Javascript is required' },
      ],
    },
  },
  css: ['@fortawesome/fontawesome-svg-core/styles.css',
    '~/assets/css/tailwind.css',
    'vuetify/styles',
    'vuetify/dist/vuetify.min.css',
    
    '@mdi/font/css/materialdesignicons.min.css',
  ],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/tailwindcss',
    ['@pinia/nuxt',
      {
        autoImports: ['defineStore', 'acceptHMRUpdate'],
      }],
    '@pinia-plugin-persistedstate/nuxt',
  ],
  // piniaPersistedstate: {
  //   cookieOptions: {
  //     sameSite: 'strict',
  //   },
  //   storage: 'localStorage'
  // },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [
      '@nuxtjs/tailwindcss',
      'nuxt/postcss8',
      '@fortawesome/fontawesome-svg-core',
      '@fortawesome/pro-solid-svg-icons',
      '@fortawesome/pro-regular-svg-icons',
      '@fortawesome/pro-light-svg-icons',
      '@fortawesome/free-brands-svg-icons',
      'vuetify'
    ]
  },
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css',
    configPath: '~/config/tailwind.js',

  },



});
