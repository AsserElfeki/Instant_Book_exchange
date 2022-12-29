<template>
  <div class="container">
    <div class="book-display flex items-center flex-wrap flex-col">
      <div class="book-container">
        <img class="book-cover rounded-md w-48 h-64 mr-5 relative" src="../../assets/img/book-cover.jpg"
          alt="cover of the book" style="left: -100%; transform: translateY(30%);"/>
          <div class="title-author-container">
           <p class="book-title">{{ store.clickedBook.title }}</p>
           </div>
          <!-- <p class="book-condition">Condition: {{ store.clickedBook.condition }}</p>
          <p class="book-condition inline">Category: </p>
          <p class = "inline" >{{store.clickedBook.category.join(', ')}}</p>
          <button class="btn block">Trade</button> -->
      </div>
    </div>
  </div>
  <div>
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
.container {
  background-image: url("../../assets/img/heroBookBackground.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 400px;
}
.title-author-container{
    position: absolute; 
    left: 40%; top: 25%; 
    transform: translateY(-50%);
    text-align: center; 
    width: 50%;
}

</style>
