<template>
    <div class="book-card flex items-center justify-between">
        <div class="overflow-hidden">
            <img :src="book.image" :alt="book.title" class="cover">
            <p class="text-[#e76f51] text-2xl h-20">{{ book.title }}</p>
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
    width: 20rem;
    height: 15rem;
    object-fit:contain;
    background-color: rgb(221,218,238); /* set the background color */
}
.book-card {

    margin: 1rem;
    padding: 1rem;
    border: 2px solid black;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    background-color:rgb(221,218,238); /* set the background color */
}
</style>