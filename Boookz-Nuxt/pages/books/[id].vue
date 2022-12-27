<template>
    <swiper
    :slides-per-view="1"
    :space-between="50"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
  >
  >
    <swiper-slide>
        <img class="rounded-md" src="../../assets/img/book-cover.jpg" alt="cover of the book">
    </swiper-slide>
    <swiper-slide>
        <img class="rounded-md " src="../../assets/img/book-cover.jpg" alt="cover of the book">
    </swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
    ...
  </swiper>
    <div class="container flex flex-col items-center rounded-2xl">
        <div class="w-3/12 rounded-md  ">
        <img class="rounded-md h-full w-full" src="../../assets/img/book-cover.jpg" alt="cover of the book">
        </div>
      <h2 class="book-title">{{ book.title}}</h2>
      <p class="book-condition">Condition: {{ book.condition }}</p>
      <p class="book-condition">Category: {{ book.category }}</p>

      <button class="btn" >Trade</button>
    </div>
</template>


<script>
import { useDataStore } from '~/stores/dataStore'
const store = useDataStore()
const book  = shallowRef (store.clickedBook)
  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
      return {
        onSwiper,
        onSlideChange,
        store,
        book,
      };
    },
  };
</script>
<style lang = 'scss' scoped>


</style>

