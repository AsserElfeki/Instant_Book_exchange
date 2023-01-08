<template>
  <div
    v-if="store.userTransactions.length"
    class="flex flex-col gap-4 justify-center "
  >
    <h2 class="font-bold text-xl m-2">My History</h2>
    <div
      v-for="(transaction, index) in store.userTransactions"
      :key="transaction.token"
      class="flex flex-col gap-2 m-2"
    >
      <h2>Date: {{ transaction.created }}</h2>
      <div class="bg-[#F2F0FE] rounded-xl p-4 flex flex-col gap-2">
        <div
          class="flex flex-row md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg">
            {{ transaction.book_reader_initiator }}
          </h3>
          <h3 class="font-bold text-lg">
            {{ transaction.initiator_book }}
          </h3>
          <font-awesome-icon
            v-if="transaction.book_reader_initiator === store.userName"
            icon="fa-solid fa-arrow-right-from-bracket"
            class="text-green-500 fa-xl"
          />
          <font-awesome-icon
            v-else
            icon="fa-solid fa-arrow-right-from-bracket"
            class="rotate-180 text-red-500 fa-xl"
          />
          <!-- sadsad  -->
        </div>
        <div
          class="flex flex-row md:flex-row justify-between bg-white border border-dashed border-black rounded-xl p-4 gap-2 items-center"
        >
          <h3 class="font-bold text-lg">
            {{ transaction.book_reader_receiver }}
          </h3>
          <h3 class="font-bold text-lg">
            {{ transaction.receiver_book }}
          </h3>
          <font-awesome-icon
            v-if="transaction.book_reader_receiver === store.userName"
            icon="fa-solid fa-arrow-right-from-bracket"
            class="text-green-500 fa-xl"
          />
          <font-awesome-icon
            v-else
            icon="fa-solid fa-arrow-right-from-bracket"
            class="rotate-180 text-red-500 fa-xl"
          />
        </div>
        <div class="flex justify-around">
          <h2 class="self-center text-violet-700 font-bold">
            Status: {{ transaction.transaction_status }}
          </h2>
          <div
            v-if="
              transaction.transaction_status === 'Initiated' &&
              transaction.book_reader_initiator !== store.userName
            "
            class="flex gap-2"
          >
            <div class="btn-sm">
              <button
                @click="acceptTransaction(transaction.token)"
              class="text-xs md:text-lg"

              >
                Accept
              </button>
            </div>
            <div class="btn-sm">
              <button
                @click="declineTransaction(transaction.token)"
              class="text-xs md:text-lg"

              >
                Decline
              </button>
            </div>
          </div>

          <div
            v-if="
              transaction.transaction_status === 'Accepted' ||
              (transaction.transaction_status ===
                'Received by initiating user' &&
                transaction.book_reader_initiator !== store.userName) ||
              (transaction.transaction_status ===
                'Received by receiving user' &&
                transaction.book_reader_receiver !== store.userName)
            "
            class="btn-sm"
          >
            <button
              @click="confirmBookRecieved(transaction.token)"
              class="text-xs md:text-lg"
            >
              I recieved the book
            </button>
          </div>

          <div
            v-if="transaction.transaction_status === 'Completed'"
            class="btn-sm"
          >
            <button @click="showComment(index)"
              class="text-xs md:text-lg"
            >Rate the transaction</button>
          </div>
        </div>
      </div>
      <div
        v-if="commentShown && index == transactionIndex"
        class=""
      >
        <form
          @submit.prevent="rateTransaction(transaction.token)"
          class="flex flex-row justify-between gap-3"
        >
          <textarea
            placeholder="comment"
            v-model="form.comment"
            class="input flex-1"
            size="200"
          />
          <fieldset class="flex items-center gap-4">
            <label for="rating">Rating:</label>
            <input
              v-model="form.rating"
              id="rating"
              type="number"
              placeholder="stars"
              max="5"
              min="1"
            />
          </fieldset>
        </form>
      </div>
    </div>
  </div>

  <div
    v-else
    class="mt-16"
  >
    <LazyProfilePlaceHolder />
  </div>
</template>

<script setup>
  import { useUserStore } from '~/stores/userStore';
  import { useProfileStore } from '~/stores/profileStore';
  const route = useRoute().params;
  const store = !route.id ? useUserStore() : useProfileStore();
  const commentShown = ref(false);
  const transactionIndex = ref();
  const form = reactive({
    rating: 0,
    comment: '',
  });

  function acceptTransaction(token) {
    store.acceptTransaction(token);
  }

  function declineTransaction(token) {
    store.declineTransaction(token);
  }

  function confirmBookRecieved(token) {
    store.confirmBookRecieved(token);
  }

  function showComment(index) {
    transactionIndex.value = index;
    commentShown.value = true;
  }
  function rateTransaction(token) {
    store.rateTransaction(token, form);
  }
</script>

<style scoped>
  .input {
    border: 2px solid black;
    border-radius: 7px;
    padding: 10px;
  }
</style>
