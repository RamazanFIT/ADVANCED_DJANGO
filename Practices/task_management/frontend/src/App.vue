<script>
import ItemList from './components/ItemList.vue'

export default {
  name: 'App',
  components: {
    ItemList
  }
}
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-title>Task Management</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn to="/register" text>Register</v-btn>
      <v-btn to="/login" text>Login</v-btn>
      <v-btn to="/admin" text>Admin</v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
.v-application {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
