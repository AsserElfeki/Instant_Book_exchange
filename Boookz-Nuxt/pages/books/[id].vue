<template>
  <div class="container">
    <swiper :slides-per-view="3" :space-between="50" @swiper="onSwiper" @slideChange="onSlideChange">
      >
      <swiper-slide>
        <img class="rounded-md" src="../../assets/img/book-cover.jpg" alt="cover of the book" />
      </swiper-slide>
      <swiper-slide>
        <img class="rounded-md" src="../../assets/img/book-cover.jpg" alt="cover of the book" />
      </swiper-slide>
      <swiper-slide>
        <img class="rounded-md" src="../../assets/img/book-cover.jpg" alt="cover of the book" />
      </swiper-slide>
      <swiper-slide>
        <img class="rounded-md" src="../../assets/img/book-cover.jpg" alt="cover of the book" />
      </swiper-slide>
      <swiper-slide>Slide 3</swiper-slide>
      ...
    </swiper>
    <div class="book-display flex items-center flex-wrap">
      <div class="book-container flex items-center">
        <img class="book-cover rounded-md w-48 h-64 mr-5" src="../../assets/img/book-cover.jpg"
          alt="cover of the book" />
        <div class="book-info flex-1">
          <h2 class="book-title">{{ store.clickedBook.title }}</h2>
          <p class="book-condition">Owner: {{ store.clickedBook.book_owner }}</p>
          <p class="book-condition">Condition: {{ store.clickedBook.condition }}</p>
          <p class="book-condition">Category: {{ store.clickedBook.category }}</p>
        </div>
        <button class="btn">Trade</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useDataStore } from "~/stores/dataStore";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
const store = useDataStore();
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
      console.log("slide change");
    };
    return {
      onSwiper,
      onSlideChange,
      store,
    };
  },
};
</script>

<style scoped>

</style>
