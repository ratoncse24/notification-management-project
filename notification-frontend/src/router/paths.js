/**
 * All application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
import store from '../store'
export default [
  {
    path: '*',
    meta: {
      name: '',
      requiresAuth: true
    },
    redirect: {
      path: '/admin/dashboard'
    }
  },
  // This  allows you to have pages apart of the app but no rendered inside the dash
  {
    path: '/',
    meta: {
      name: 'Website View',
      requiresAuth: false
    },
    component: () => import(`@/views/EcommerceView.vue`),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import(`@/components/Home.vue`)
      }
    ]
  },
  {
    path: '/admin/login',
    meta: {
      name: '',
      requiresAuth: false
    },
    component: () =>
      import(/* webpackChunkName: "routes" */ `@/views/LoginHome.vue`),
    // redirect if already signed in
    beforeEnter: (to, from, next) => {
      if (store.getters.authorized) {
        next('/admin/dashboard')
      } else {
        next()
      }
    },
    children: [
      {
        path: '',
        component: () => import(`@/components/LoginForm.vue`)
      }
    ]
  },
  {
    path: '/admin/dashboard',
    meta: {
      name: 'Dashboard View',
      requiresAuth: true
    },
    component: () => import(`@/views/DashboardView.vue`),
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: () => import(`@/components/DashViews/Dashboard.vue`)
      }
    ]
  },
  {
    path: '/admin/notifications',
    meta: {
      name: 'Notification View',
      requiresAuth: true
    },
    component: () => import(`@/views/DashboardView.vue`),
    children: [
      {
        path: '',
        meta: {
          name: 'Notifications',
          requiresAuth: true
        },
        component: () => import(`@/components/NotificationViews/Notifications.vue`)
      }
    ]
  }
]
