<template>
    <div class="header flex flex-col justify-between items-center py-8">
        <img src="../assets/img/avatar.png" alt="profile avatar" class="">
        <h2 class="text-white font-sans text-2xl font-bold">{{ userStore.userName }}</h2>
        <h3 class="text-white font-sans font-thin"> {{ userStore.region }}</h3>

        <div class="tabs mt-8 bg-white rounded-md h-24 w-11/12 flex justify-around items-center ">
            <button class="tab mx-7 w-18 h-20 px-2 rounded-md" @click="toggleTabs($event)">Giveaway Shelf</button>
            <button class="tab mx-7 w-18 h-20 px-2 rounded-md" @click="toggleTabs($event)">Wanted Shelf</button>
            <button class="tab mx-7 w-18 h-20 px-2 rounded-md" @click="toggleTabs($event)">Transactions</button>
            <button class="tab mx-7 w-18 h-20 px-2 rounded-md" @click="toggleTabs($event)">Ratings</button>

        </div>
    </div>
</template>




<script setup>
import { useUserStore } from '~~/stores/userStore';
const userStore = useUserStore();


//a function that adds class active to the button that fired the event
function toggleTabs(event) {
    let array = document.getElementsByClassName("tab");
    for (let i = 0; i < array.length; i++) {
        array[i].classList.remove("active");
    }
    event.target.classList.add("active")
}

</script>

<style  scoped>
.header {
    height: 500px;
    background: linear-gradient(93.97deg, #695AC9 0.68%, #925AC9 98.66%);
}

.active {
    background: #D4CDFF;
}
</style>


//ToDO: 
// 1. figure out the change in clicking 
// 2. figure out how to make the tabs responsive
// 3. figure out how to make the tabs active
// 4. figure out how to make the tabs change the content
