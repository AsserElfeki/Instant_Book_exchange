<template>
  <div class="container">
    <div class="book-display flex items-center flex-wrap flex-col">
      <div class="book-container">
        <img class="book-cover rounded-md w-48 h-64 mr-5 static" :src="store.clickedBook.images.at(0)"
          alt="cover of the book" style="left: -100%; transform: translateY(30%);"/>
          <div class="book-info-container">
            <h1 class = "book-title font-bold font-serif text-xl" >{{store.clickedBook.title}}</h1>
            <p class="book-authors">By: {{ store.clickedBook.author.join(', ')}}</p>
            <p class="book-condition inline">Category: </p>
            <p class = "inline" >{{store.clickedBook.category.join(', ')}}</p>
             <p class="book-condition">Condition: {{ store.clickedBook.condition }}</p>
           </div>
      </div>
    </div>
  </div>
  <br /><br />
    <hr class ="separator w-4/5"/>
    <br /><br />
  <div class=" book-description-section">
    <h1 class = "font-bold font-serif text-3xl" >Description:</h1>
    <br />
    <p class="book-description text-xl"> {{ store.clickedBook.description }}</p>
    <br /><br />
    <hr class ="separator w-4/5"/>
    <br /><br />
    </div>
  <div>
    <h1 class = "font-bold font-serif text-3xl" >Images:</h1>
<br />
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
    <hr class ="separator w-full"/>
    <br /><br />
</div>
<div>
    <h1 class = "font-bold font-serif text-3xl inline mr-3" >Offered By: </h1>
    <p class ="inline mr-3">{{store.clickedBook.book_owner.at(0)}}</p>
    <img class="user-image w-16 h-16 rounded-full border-black border inline" :src="store.clickedBook.book_owner.at(1)" alt="user profile picture" >
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
.book-info-container{
    position: relative; 
    left: 50%; 
    transform: translateY(-100%);
    text-align: left; 
    width: 50%;
}

</style>
