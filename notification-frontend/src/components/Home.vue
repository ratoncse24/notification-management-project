<template>
      <v-container
        class="fill-height"
        fluid
      >
     <v-layout wrap>
      
      <v-flex
        md3
        sm3
        lg3
        v-for="(product, index) in products" :key="index"
      >
         <v-card>
                <v-img
                  :src="product_image"
                  class="white--text align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="200px"
                  contain
                >
                  <v-card-title v-text="product.name"></v-card-title>
                </v-img>
    
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <div class="my-2">
                    <v-btn small color="primary" >Buy Now</v-btn>
                  </div>
                </v-card-actions>
              </v-card>
      </v-flex>
       
    </v-layout>

      </v-container>
</template>

<script>
  export default {
      created () {
    this.initialize()
  },

  methods: {
    initialize () {
      this.detectCurrentUserVisit();
    },

    detectCurrentUserVisit(){
      // set or update cookie for the website visitor
        let user_info = this.$cookies.getJSON('myapp-user')
        if (user_info == undefined){
          this.setNewCookie()
        }else{
          this.updateVisitCookie()
          // this.updatePurchasedCookie()
        }
        this.checkCookieForNotification()
    },
    checkCookieForNotification(){
      // detect current user and show the relevent notification to the visitor
        let user_info = this.$cookies.getJSON('myapp-user')
        let first_visit = this.$moment(user_info.first_visit_date, "YYYY-MM-DD  h:mm:ss a")
        let last_visit = this.$moment().diff(first_visit, 'months')
        let notification_event = '';
        if(user_info.visit_count == 1){
            notification_event = '1st-visit';
        }else if(user_info.visit_count == 2){
          notification_event = '2nd-visit';
        }else if(last_visit >= 1){
          notification_event = 'old-user-after-1-month';
        }else if(user_info.purchased == true){
          notification_event = 'after-purchase-and-revisited';
        }

      if(notification_event != ''){
        this.getEventNotificationText(notification_event);
      }
    },

    getEventNotificationText(event){
      // Get notification text from server using event name
      this.$http.get('notification/event/'+event)
        .then((response) => {
          var data = response.data;
          console.log(data)
          if(data.notification_text !== undefined){
            this.showNotification(data.notification_text);
          }
        })
        .catch(err => {
          console.log(err)
        })

    },
    setNewCookie(){
      // set initial cookie when user visit first time
        let today = this.$moment().format('YYYY-MM-DD h:mm:ss a');
        let visit_count = 1;
        let purchased = false;
       this.$cookies.set('myapp-user', { first_visit_date: today, visit_count: visit_count, purchased: purchased });
    },
    updateVisitCookie(){
      // increment visit_count cookie variable and update to cookie object
        let user_info = this.$cookies.getJSON('myapp-user')
        let visit_count = user_info.visit_count + 1;
        this.$cookies.set('myapp-user', { first_visit_date: user_info.first_visit_date, visit_count: visit_count, purchased: user_info.purchased });
    },
    updatePurchasedCookie(){
      // set purchased true when user purchases anything from this website
        let purchased = true;
        let user_info = this.$cookies.getJSON('myapp-user')
        this.$cookies.set('myapp-user', { first_visit_date: user_info.first_visit_date, visit_count: user_info.visit_count, purchased: purchased });
    },
    showNotification (message) {
      // Show notification to the user
      this.$notify({
        group: 'visitor-notification',
        type: 'success',
        duration: -1,
        closeOnClick: false,
        ignoreDuplicates: true,
        // title: 'Important message',
        text: message
      });
    }
  },
    data: () => ({
      product_image: require('@/assets/img/product.png'),
      products: [
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"},
        {'name': "Demo Product"}
      ]
    })
  }
</script>


