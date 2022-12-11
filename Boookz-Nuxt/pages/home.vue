<template>
    <div class="container">
       
        <div class="hero max-w-full">
            <HeroBg></HeroBg>
            <RandomBook />
        </div>
        <div class="allgiveaways">
            <h2>Offered by our users in your area</h2>
            <div class="showcase">
                <!-- <div class="book" v-for="book in books"></div> -->
                <!-- books -->
            </div>
        </div>
        <div class="allwanted">
            <h2>Wanted by users in your area</h2>
            <div class="book-info">
                {{ books }}
            </div>
            <div class="showcase">
                <!-- books -->
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.hero {
    border: 2px solid blue;
    overflow: hidden;
}





</style>



