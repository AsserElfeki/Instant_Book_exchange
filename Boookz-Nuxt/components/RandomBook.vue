<template>
    <div class="container">
        <div class="book">
            <div class="book-img">
                <!-- <img :src="bookImg" alt="book image"> -->
                <h1>random book</h1>
            </div>
            <div class="book-info">
                <h2>{{ book.title }}</h2>
                <h3>{{ book.author }}</h3>
                <h4>{{ book.category }}</h4>
                <p>{{ book.description }}</p>
                <div class="book-rating">
                    <!-- <p>{{ bookRating }}</p> -->
                </div>
                <div class="book-price  ">
                    <!-- <p>{{ bookPrice }}</p> -->
                </div>
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
    background-image: "../assets/img/heroBackground.jpg";
    
}
</style>




