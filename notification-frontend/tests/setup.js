import Vue from 'vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex'
import axios from 'axios'
import Notifications from 'vue-notification'
import store from '@/store'
Vue.use(Vuetify);
Vue.use(Vuex)
// Vue.use(Notifications)

// Vue.prototype.$http = axios
// Vue.prototype.$store = store
Vue.config.productionTip = false;
document.body.setAttribute('data-app', true)
