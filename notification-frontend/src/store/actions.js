// https://vuex.vuejs.org/en/actions.html
import axios from 'axios'
import Vue from 'vue'
// The login action passes vuex commit helper that we will use to trigger mutations.
export default {
  login ({ commit }, userData) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      axios.post('/obtain_token', { username: userData.username, password: userData.password })
        .then(response => {
          const token = response.data.access_token
          const refresh_token = response.data.refresh_token
          const user = {name: ''}
          console.log(response)
          // storing jwt in localStorage. https cookie is safer place to store
          localStorage.setItem('token', token)
          localStorage.setItem('refresh_token', refresh_token)
          localStorage.setItem('user', user)
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
          // mutation to change state properties to the values passed along
          commit('auth_success', { token, user })
          resolve(response)
        })
        .catch(err => {
          console.log('login error')
          commit('auth_error')
          localStorage.removeItem('token')
          reject(err)
        })
    })
  },
  logout ({ commit }) {
    return new Promise((resolve, reject) => {
      commit('logout')
      localStorage.removeItem('token')
      localStorage.removeItem('refresh_token')
      delete axios.defaults.headers.common['Authorization']
      resolve()
    })
  },
  refreshtoken ({ commit },) {
    const refresh_token = localStorage.getItem('refresh_token')
    axios.defaults.headers.common['Authorization'] = 'Bearer ' +refresh_token
    axios.post('/refresh_token')
      .then(response => {
        const token = response.data.access_token
        localStorage.setItem('token', token)
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
        commit('auth_success', { token })
      })
      .catch(error => {
        console.log('refresh token error')
        commit('logout')
        localStorage.removeItem('token')
        console.log(error)
      })
  },
  callApi ({commit}, info) {
    console.log(info)
    return new Promise((resolve, reject) => {
      Vue.prototype.$http({ url: info.endpoint, method: info.method, data: info.data })
      .then(response => {
        commit('callApi')
        console.log(response)
        resolve(response)
      })
      .catch(error => {
        console.log(error)})
    })
  }


}
