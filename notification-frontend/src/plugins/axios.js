// Lib imports
import axios from 'axios'

// Sets the default url used by all of this axios instance's requests
axios.defaults.baseURL = 'http://facelbook.com/'

const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = token
}
