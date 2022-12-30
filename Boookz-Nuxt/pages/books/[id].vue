<template>
  <div v-if="book" class="flex flex-col justify-center border-2 border-red-400">
    <div
      class="hero bg-gradient-to-r from-violet-100 to-violet-700 h-auto rounded-2xl p-2"
    >
      <div
        class="flex flex-col md:flex-row md:flex-nowrap justify-center md:justify-around items-center gap-8"
      >
        <img
          class="rounded-2xl h-60 md:h-auto border-2 border-blue-500"
          :src="book.images.at(0)"
          alt="cover of the book"
        />
        <div class="flex flex-col gap-2 border-2 border-blue-500">
          <h1 class="font-bold font-serif text-xl leading-none">{{ book.title }}</h1>
          <p class="">By: {{ book.author.join(", ") }}.</p>
          <div>
            <p class="inline">Category:</p>
            <p class="inline">{{ book.category.join(", ") }}.</p>
          </div>
          <p class="">Condition: {{ book.condition }}.</p>
        </div>
      </div>
    </div>
    <hr class="separator" />
    <div class="px-4">
      <h1 class="font-bold font-serif text-3xl">Description:</h1>
      <br />
      <p class="flex md:text-xl">{{ book.description }}</p>
      <hr class="separator" />
    </div>
    <div class="px-4 mx-auto w-full">
      <h1 class="font-bold font-serif text-3xl">Images:</h1>
      <br />
      <swiper
        :slides-per-view="1"
        :space-between="50"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        class="border-2 border-black flex justify-center items-center w-1/3"
      >
        >
        <swiper-slide v-for="n in book.images.length">
          <img class="rounded-md" :src="book.images.at(n - 1)" alt="cover of the book" />
        </swiper-slide>
        
        <swiper-slide v-for="n in book.images.length">
          <img class="rounded-md" :src="book.images.at(n - 1)" alt="cover of the book" />
        </swiper-slide>
        <swiper-slide v-for="n in book.images.length">
          <img class="rounded-md" :src="book.images.at(n - 1)" alt="cover of the book" />
        </swiper-slide>
      </swiper>
      <hr class="separator" />
    </div>
    <div>
      <h1 class="font-bold font-serif md:text-3xl inline mr-3">Offered By:</h1>
      <p class="inline mr-3 md:text-xl">{{ book.book_owner.at(0) }}</p>
      <img
        class="user-image w-16 h-16 rounded-full border-black border inline"
        :src="book.book_owner.at(1)"
        alt="user profile picture"
      />
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
  data() {
    return { book: "" };
  },
  mounted() {
    const store = useDataStore();
    this.book = store.clickedBook;
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
    };
  },
};
</script>

<style scoped>
.hero {
  /* background-image: url("../../assets/img/heroBookBackground.png"); */
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  /* height: 400px; */
}
</style>
