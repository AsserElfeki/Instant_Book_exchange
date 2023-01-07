/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './components/**/*.{js,vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './nuxt.config.{js,ts}',
    './app.vue',
  ],
  theme: {
    colors: {
      'primary': '#00ff00',

    },
    extend: {
      colors: {
      },
    },
  },
  plugins: [],
  important: true
};
