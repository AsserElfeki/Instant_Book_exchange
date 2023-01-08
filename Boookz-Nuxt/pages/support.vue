<template>
  <div>
    <form
      @submit.prevent="sendToSupport"
      class="flex flex-col items-center justify-center p-4"
    >
      <div class="border-4 border-violet-200 rounded-xl p-4 w-3/4 flex justify-center">
        <textarea
          class="w-full text-xl outline-none"
          placeholder="Enter your message here"
          v-model="message"
          rows="5"
        >
        </textarea>
      </div>

        <button
            type="submit"
            class="mt-4 bg-violet-400 hover:bg-violet-500 text-white font-bold py-2 px-4 rounded"
        >submit
        </button>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from '~/stores/userStore';
const userStore = useUserStore();
const message = ref('')
function sendToSupport () {
userStore.sendToSupport(message.value)
};


</script>

<style scoped></style>
