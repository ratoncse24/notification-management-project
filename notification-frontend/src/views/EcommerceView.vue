<template>
  <v-app id="inspire">

    <v-toolbar
      app
      color="orange"
      dark
    >
      <v-toolbar-title>E-Commerce </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <transition mode="out-in">
        <router-view/>
      </transition>
    </v-content>


    <v-footer
      color="orange"
      app
    >
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
      <v-spacer></v-spacer>
</v-footer>
  </v-app>
</template>

<script>
  export default {

  }
</script>
