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
     <br /><br />
    <hr class ="separator w-4/5"/>
    <br /><br />
    <div class="book-display flex items-start flex-wrap flex-col">
      <div class="book-container flex items-center">
        <img class="book-cover rounded-md w-48 h-64 mr-5" src="../../assets/img/book-cover.jpg"
          alt="cover of the book" />
        <div class="book-info flex-1">
           <p class="book-title">{{ store.clickedBook.title }}</p>
          <p class="book-condition">Condition: {{ store.clickedBook.condition }}</p>
          <p class="book-condition inline">Category: </p>
          <p v-for="category in store.clickedBook.category" :key="category" class ="inline">{{category}}, </p>
          <button class="btn block">Trade</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useDataStore } from "~/stores/dataStore";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    const store = useDataStore();
    return {
      store,
    };
  },
};
</script>

<style scoped>

</style>
