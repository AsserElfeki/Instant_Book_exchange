<template>
    <div class="container flex flex-col justify-center items-center rounded-2xl">

        <h3 class="self-start ml-3 text-[#695AC9]">#suggested for YOU</h3>

        <div class="flex justify-center items-center mx-16 ">

            <div class="">
                <h3 class="text-xl text-black text-center">{{ book.title }}</h3>
                <h3 class="text-center text-lg">By: {{ book.author }}</h3>
                <!-- <h4>{{ book.category }}</h4> -->
                <p class="mt-4">{{ book.description }}</p>
                <div class="book-rating">
                    <!-- <p>{{ bookRating }}</p> -->
                </div>
                <div class="book-price  ">
                    <!-- <p>{{ bookPrice }}</p> -->
                </div>
            </div>

            <div class="w-full ml-4 rounded-md  ">
                <img class="rounded-md h-full w-full" src="../assets/img/book-cover.jpg" alt="cover of the book">
            </div>

        </div>
    </div>
</template>

<script setup>
const { book } = defineProps(['book'])

console.log("random book:", book)
</script>

<style scoped>
.container {
    background-image: url("../assets/img/heroBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    height: 400px;
}
</style>




