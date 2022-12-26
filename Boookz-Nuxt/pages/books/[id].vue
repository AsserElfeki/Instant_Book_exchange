<template>
    <div>
      <BookCard :book="store.clickedBook" />
    </div>
</template>

<script setup>
import { useDataStore } from '~/stores/dataStore'
const { id } = useRoute().params

const store = useDataStore()
definePageMeta({
        // layout: 'books'
    })
</script>

<style scoped>

</style>

