<template>
    <div class="book-card ">
        <div class="overflow-hidden border-green-500 border-2 border-solid">
            <img :src="book.image" :alt="book.title" class="cover">
        </div>
        <div>
            <p class="text-[#e76f51] text-2xl">{{ book.title }}</p>
            <p class="text-lg">Author: {{ book.author }}</p>
            <p class="">{{ book.description }}</p>
            <p class="text-secondary text-lg my-3">{{ book.points }} point</p>
            <p>Offered by: {{ book.owner }}</p>
            <button class="btn">Get it</button>

        </div>
    </div>
</template>

<script setup>
const { book } = defineProps(['book'])
</script>

<style  scoped>
.cover {
    display:block;
    width: 10rem;
    height: 2 0rem;
    object-fit:cover;
}
</style>