<template>
    <div
        class="book-card my-4 shadow-xl border-2 border-solid border-black relative rounded-3xl flex items-center overflow-visible">
        <div class="rounded-3xl">
            <img :src="book.images.at(0)" :alt="book.title" class="cover rounded-3xl w-full object-contain">

            <p class="text-[#e76f51] text-xl h-20">{{ book.title }}</p>
            <div CLASS="flex justify-between my-2">
                <p> by: {{ book.book_owner.at(0) }}</p>
                <button class="btn-sm">Trade</button>
            </div>
        </div>
        <img :src="book.book_owner.at(1)" :alt="book.title"
            class="user-image w-16 h-16 rounded-full object-cover absolute left-1/2 border-black border">
    </div>
</template>

<script setup>
const { book } = defineProps(['book'])
</script>

<style  scoped>
.covere {
    width: 20rem;
    height: 15rem;
    object-fit: contain;
    background-color: rgb(221, 218, 238);
    /* set the background color */
}

.book-card {
    /* position: relative; */
    /* margin: 1rem;
    padding: 1rem; */
    /* border: 2px solid black; */
    /* border-radius: 20px; */
    /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); */
    background-color: rgb(221, 218, 238);
    overflow: visible;
}

.user-image {
    bottom: -40px;
    transform: translateX(-50%);
}
</style>
