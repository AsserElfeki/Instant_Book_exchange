<template>
    <div
        class="bg-[#dddaee] my-4 max-w-xs shadow-xl  relative rounded-3xl flex flex-col items-center overflow-visible p-3">
        <div class="rounded-3xl w-full max-h-[800px]">
            <img :src="book.images.at(0)" :alt="book.title" class="cover rounded-3xl w-full max-h-40 object-contain">

            <p class="text-[#e76f51] text-sm md:text-xl h-20">{{ truncate(book.title, 30) }}</p>
            <div class="flex justify-between my-2 min-w-full ">
                <p class="text-sm md:text-lg"> by: {{ book.book_owner.at(0) }}</p>
            </div>
        </div>
        <img :src="book.book_owner.at(1)" :alt="book.title"
            class="user-image w-16 h-16 rounded-full object-cover absolute bottom-[-40px] left-1/2 -translate-x-1/2 border-black border">
    </div>
</template>

<script setup>
const { book } = defineProps(['book'])
function truncate(string, value) {
    if (string.length > value)
        return string.substring(0, value) + '…';
    else
        return string;
}
</script>