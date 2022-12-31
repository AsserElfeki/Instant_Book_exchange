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
        :modules="modules"
        :slides-per-view="1"
        :space-between="50"
        navigation
        :pagination="{ clickable: true }"
        :scrollbar="{ draggable: true }"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        class="border-2 border-black flex justify-center items-center w-1/3"
      >
        >
        <swiper-slide v-for="n in book.images.length">
          <img class="rounded-md" :src="book.images.at(n - 1)" alt="cover of the book" @click="showImage(book.images.at(n - 1))" />
        </swiper-slide>

        <swiper-slide v-for="n in book.images.length">
          <img class="rounded-md" :src="book.images.at(n - 1)" alt="cover of the book" @click="showImage(book.images.at(n - 1))"/>
        </swiper-slide>
      </swiper>
      <div v-if="showModal" class="modal-overlay" @click="hideModal">
         <img :src="modalImage" class="modal-image" />
        </div>
      <hr class="separator" />
    </div>

    <div>
      <h1 class="font-bold font-serif md:text-3xl inline mr-3 ml-3">Offered By:</h1>
      <p class="inline mr-3 md:text-xl">{{ book.book_owner.at(0) }}</p>
      <img
        class="user-image w-16 h-16 rounded-full border-black border inline"
        :src="book.book_owner.at(1)"
        alt="user profile "
      />
    </div>
    <button class="btn-sm w-28 mb-4 m-auto">Trade</button>
  </div>
</template>

<script>
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
import { useDataStore } from "~/stores/dataStore";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return { book: "" };
  },
  methods: {
    showImage(image) {
      this.showModal = true
      this.modalImage = image
      console.log("Show Image");

    },
    hideModal() {
      this.showModal = false
      console.log("Hide Image");
    }

  },
  mounted() {
    const store = useDataStore();
    this.book = store.clickedBook;
    
  },
  setup() {
    const showModal = false
    const modalImage = ''
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log("slide change");
    };
    return {
      onSwiper,
      onSlideChange,
      modules: [Navigation, Pagination, Scrollbar, A11y],
      showModal,
     modalImage
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
.swiper-pagination {
    position: absolute;
    bottom: 20px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
  }
  .modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-image {
  max-width: 80%;
  max-height: 80%;
}
</style>
