// https://vuex.vuejs.org/en/state.html

export default {
  authStatus: '',
  token: localStorage.getItem('token') || '',
  refresh_token: localStorage.getItem('refresh_token') || '',
  user: localStorage.getItem('user') || {}
}
