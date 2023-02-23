<template>
  <div
      v-if="book"
      class="flex flex-col justify-center"
  >
    <div
        class="hero bg-gradient-to-r from-violet-100 to-violet-700 h-auto rounded-2xl p-2"
    >
      <div
          class="flex flex-col md:flex-row md:flex-nowrap justify-center md:justify-around items-center gap-8"
      >
        <img
            class="rounded-2xl h-60 md:h-96"
            :src="book.images.at(0)"
            alt="cover of the book"
        />
        <div class="flex flex-col gap-2">
          <h1 class="font-bold font-serif text-xl leading-none">
            {{ book.title }}
          </h1>
          <p class="">By: {{ book.author.join(', ') }}</p>
          <div>
            <p class="inline">Category:</p>
            <p class="inline">{{ book.category.join(', ') }}</p>
          </div>
          <p class="">Condition: {{ book.condition }}</p>
          <p class="">Language: {{ book.language }}</p>
        </div>
      </div>
    </div>
    <hr class="separator"/>
    <div class="px-4">
      <h1 class="font-bold font-serif text-3xl">Description:</h1>
      <br/>
      <p class="flex md:text-xl">{{ book.description }}</p>
      <hr class="separator"/>
    </div>
    <div class="px-4 mx-auto w-full">
      <h1 class="font-bold font-serif text-3xl">Images:</h1>
      <br/>
      <swiper
          :modules="modules"
          :slides-per-view="1"
          :space-between="100"
          navigation
          :pagination="{ clickable: true }"
          :scrollbar="{ draggable: true }"
          @swiper="onSwiper"
          @slideChange="onSlideChange"
          class="flex justify-center items-center w-1/3"
      >
        <swiper-slide
            v-for="n in book.images.length"
            class="flex flex-row items-center justify-center"
        >
          <img
              class="rounded-md object-contain"
              :src="book.images.at(n - 1)"
              alt="cover of the book"
              @click="showImage(book.images.at(n - 1))"
              style="max-height: 500px; max-width: 500px"
          />
        </swiper-slide>
      </swiper>
      <div
          v-if="showModal"
          class="modal-overlay"
          @click="hideModal"
      >
        <img
            :src="modalImage"
            class="modal-image"
        />
      </div>
    </div>
    <hr class="separator"/>

    <div
        v-if="username !== book.book_owner.username"
        class="flex items-center gap-2 md:gap-32 justify-start"
    >
      <div class="flex items-baseline justify-center">
        <h1 class="font-bold md:text-2xl inline mr-3 ml-3">Owner:</h1>
        <NuxtLink
            :to="`/profile/${book.book_owner.username.replaceAll(' ', '-')}`"
            class="cursor-pointer rounded-xl"
        >
          <p class="inline mr-3 md:text-xl font-bold">
            {{ book.book_owner.username }}
          </p>
          <img
              v-if="book.book_owner.profile_image"
              :src="book.book_owner.profile_image"
              :alt="book.book_owner.username"
              class="user-image w-10 h-10 rounded-full border-black border inline"
          />
          <img
              v-else
              src="../../assets/img/avatar.png"
              alt="profile avatar"
              class="user-image w-16 h-16 rounded-full border-black border inline"
          />
        </NuxtLink>
      </div>
      <div
          v-if="userStore.userIsLoggedIn && userCanTradeBook"
          class="btn"
      >
        <button
            class="w-20"
            @click="setShowTrade"
        >
          Trade
        </button>
      </div>
    </div>
    <div v-if="showTrade">
      <LazyTrade/>
    </div>
  </div>
</template>
<script>
import {Navigation, Pagination, Scrollbar, A11y} from 'swiper';
import {useDataStore} from '~/stores/dataStore';
import {useUserStore} from '~/stores/userStore';
import {Swiper, SwiperSlide} from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      book: '',
      username: '',
      loginSatus: false,
      showModal: false,
      showTrade: false,
    };
  },
  methods: {
    showImage(image) {
      this.showModal = true;
      this.modalImage = image;
      console.log('Show Image');
    },
    setShowTrade() {
      this.showTrade = true;
      console.log('show Trade');
    },
    hideModal() {
      this.showModal = false;
      console.log('Hide Image');
    }
  },
  mounted() {
    const store = useDataStore();
    this.book = store.clickedBook;
    this.loginSatus = this.userStore.userIsLoggedIn;
    this.username = this.userStore.userName;
  },
  setup() {
    const store = useDataStore();
    const userStore = useUserStore();
    const modalImage = '';
    const userCanTradeBook = ref(false);

    const onSwiper = (swiper) => {
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    if (store.clickedBook.book_shelf === "wanted") {
      for (let i in userStore.userGiveAwayBooks) {
        let userBook = userStore.userGiveAwayBooks[i];
        if (userBook.title === store.clickedBook.title) {
          userStore.chosenBookForATrade = userBook
          userCanTradeBook.value = true;
          break;
        }
        console.log('user does not have a book');
      }
    } else {
      userCanTradeBook.value = true;
    }
    return {
      onSwiper,
      onSlideChange,
      modules: [Navigation, Pagination, Scrollbar, A11y],
      modalImage,
      userStore,
      store,
      userCanTradeBook,
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
