<template>
    <div class="container">
        <div class="book">
            <div class="book-img">
                <!-- <img :src="bookImg" alt="book image"> -->
            </div>
            <div class="book-info">
                <h2>{{ book.Title }}</h2>
                <h3>{{ book.Author }}</h3>
                <h4>{{ book.Genre }}</h4>
                <p>{{ book.Description }}</p>
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
</script>

<style scoped>

</style>




