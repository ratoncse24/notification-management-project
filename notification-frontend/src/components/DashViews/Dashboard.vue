<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex
        md12
        sm12
        lg12
      >
         <h3 class="welcome-heading">{{ welcome_heading }}</h3>
         <h4 class="welcome-info">{{ welcome_info }}</h4>
      </v-flex>
       
 
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      welcome_heading: "Welcome Admin",
      welcome_info: "Manage Website Notifications"
    }
  },
  methods: {
  }
}
</script>
