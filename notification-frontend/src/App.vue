<template>
  <transition-group mode="out-in">
    <notifications group="notification"  position="top right" key="1" />
     <notifications group="visitor-notification" position="top right"  key="2">
      <template slot="body" slot-scope="props">
        <div>
          <v-alert
            v-model="show_alert"
            border="left"
            close-text="Close Alert"
            color="primary"
            dark
            dismissible
          >
            {{ props.item.title }}
            <span class="notification-text" v-html="props.item.text"></span>
          </v-alert>
        </div>
      </template>
    </notifications>
    <router-view key="3" />
  </transition-group>
</template>

<style lang="scss">
	@import "@/styles/index.scss";

	/* Remove in 1.2 */
	.v-datatable thead th.column.sortable i {
		vertical-align: unset;
	}
</style>
<script>
// checks to see if auth jwt token is valid or has expired, if it gets back 401 error log out
export default {
  data: () => ({
    show_alert: true,
  }),
  created: function () {
    this.$http.interceptors.response.use((response) => {
      return response
    }, (error) => {
      if (error.response.status === 401) {
        if (this.$store.getters.authorized) {
          this.$store.dispatch('refreshtoken')
        } else {
          return Promise.reject(error)
        }
      } else {
        return Promise.reject(error)
      }
    })
  }
}
</script>
