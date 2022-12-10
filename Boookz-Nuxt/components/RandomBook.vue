<template>
    <div class="container">
        <div class="book">
            <div class="book-img">
                <img :src="bookImg" alt="book image">
            </div>
            <div class="book-info">
                <h2>{{ bookTitle }}</h2>
                <h3>{{ bookAuthor }}</h3>
                <h4>{{ bookGenre }}</h4>
                <p>{{ bookDescription }}</p>
                <div class="book-rating">
                    <p>{{ bookRating }}</p>
                </div>
                <div class="book-price  ">
                    <p>{{ bookPrice }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>




