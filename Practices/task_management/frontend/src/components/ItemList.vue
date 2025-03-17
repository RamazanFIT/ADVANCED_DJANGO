<template>
  <v-container>
    <v-card>
      <v-card-title>Items</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="item in items" :key="item.id">
            <v-list-item-title>{{ item.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ item.description }}</v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-card-text>
      <v-card-actions>
        <v-form @submit.prevent="addItem" class="d-flex flex-column w-100">
          <v-text-field v-model="newItem.name" label="Name" required></v-text-field>
          <v-text-field v-model="newItem.description" label="Description" required></v-text-field>
          <v-btn color="primary" type="submit">Add Item</v-btn>
        </v-form>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { getItems, createItem } from '../api';

export default {
  data() {
    return {
      items: [],
      newItem: { name: '', description: '' },
    };
  },
  async created() {
    this.items = await getItems();
  },
  methods: {
    async addItem() {
      const item = await createItem(this.newItem);
      this.items.push(item);
      this.newItem = { name: '', description: '' };
    },
  },
};
</script>

<style scoped>
form {
  margin-top: 20px;
}

input {
  margin-right: 10px;
  padding: 5px;
}

button {
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 4px;
}
</style> 