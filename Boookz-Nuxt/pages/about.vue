<template>
  <div class="text-center my-12 py-12">
    <v-menu class="red">
      <template v-slot:activator="{ props: menu }">
        <v-tooltip
          location="top"
          
        >
          <template v-slot:activator="{ props: tooltip }">
            <v-btn
              color="primary"
              v-bind="mergeProps(menu, tooltip)"
            >
              Dropdown w/ Tooltip
            </v-btn>
          </template>
          <span>fbvnhdfgnh </span>
        </v-tooltip>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          dark
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-combobox
  label="Combobox"
  :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
></v-combobox>
  </div>
</template>

<script>
  import { mergeProps } from 'vue';

  export default {
    data: () => ({
      items: [
        { title: 'Click Me1' },
        { title: 'Click Me2' },
        { title: 'Click Me3' },
        { title: 'Click Me4' },
      ],
    }),
    methods: {
      mergeProps,
    },
  };
</script>
