
/**
 * Vue Router
 *
 * @library
 *
 * https://router.vuejs.org/en/
 */

// Lib imports
import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import Meta from 'vue-meta'

// Routes
import paths from './paths'

Vue.use(Router)

// Create a new router
const router = new Router({
  base: '/',
  mode: 'history',
  routes: paths
})

// Route guard checks to see if you are logged in, if not reroutes to login
// to is where you are going, matched.some is to find which routes have requiresAuth
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.authorized) {
      next()
      return
    }
    next('/admin/login')
  } else {
    next()
  }
})

Vue.use(Meta)

export default router
