<template>
  <div class="container">
    <div class="book-display flex items-center flex-wrap flex-col">
      <div class="book-container">
        <img class="book-cover rounded-md w-48 h-64 mr-5 static" :src="book.images.at(0)"
          alt="cover of the book" style="left: -100%; transform: translateY(30%);"/>
          <div class="book-info-container">
            <h1 class = "book-title font-bold font-serif text-xl inline" >{{store.clickedBook.title}}</h1>
            <p class="book-authors">By: {{ book.author.join(', ')}}</p>
            <p class="book-condition inline">Category: </p>
            <p class = "inline" >{{book.category.join(', ')}}</p>
             <p class="book-condition">Condition: {{ book.condition }}</p>
           </div>
      </div>
    </div>
  </div>
  <br /><br />
    <hr class ="separator"/>
    <br /><br />
  <div class=" book-description-section">
    <h1 class = "font-bold font-serif text-3xl" >Description:</h1>
    <br />
    <p class="book-description text-xl"> {{ book.description }}</p>
    <br /><br />
    <hr class ="separator"/>
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
    <hr class ="separator"/>
    <br /><br />
</div>
<div>
    <h1 class = "font-bold font-serif text-3xl inline mr-3" >Offered By: </h1>
    <p class ="inline mr-3 text-xl">{{book.book_owner.at(0)}}</p>
    <img class="user-image w-16 h-16 rounded-full border-black border inline" :src="book.book_owner.at(1)" alt="user profile picture" >
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
    const book= store.clickedBook;
    return {
      store,
      book,
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
.separator{
    width: 100%;
}

</style>
