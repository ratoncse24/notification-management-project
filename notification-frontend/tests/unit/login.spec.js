import { mount, shallowMount, createLocalVue } from '@vue/test-utils'
import Vuetify from 'vuetify';
import Vue from 'vue';
import LoginForm from '@/components/LoginForm.vue'

describe('LoginForm', () => {

    it('login button should disabled when username is empty', async () => {
    
        const wrapper = mount(LoginForm)
        try {
          wrapper.setData({ 'username': '' })
          wrapper.setData({ 'password': 'admin' })
          await Vue.nextTick() 

          const button = wrapper.find('#submit')
          await Vue.nextTick()
    
          expect(button.attributes().disabled).toBe('disabled')
        } finally {
          wrapper.destroy()
        }
      })

      it('login button should disabled when password is empty', async () => {
    
        const wrapper = mount(LoginForm)
        try {
          wrapper.setData({ 'username': 'admin' })
          wrapper.setData({ 'password': '' })
          await Vue.nextTick() 

          const button = wrapper.find('#submit')
          await Vue.nextTick()
    
          expect(button.attributes().disabled).toBe('disabled')
        } finally {
          wrapper.destroy()
        }
      })

      it('trigger login function when click on submit button', async () => {
    
        const login = jest.fn()
        const wrapper = mount(LoginForm, {
            methods: {
                login: login
            }
        })
        try {
          wrapper.setData({ 'username': 'admin' })
          wrapper.setData({ 'password': 'admin' })
          await Vue.nextTick() 
        //   wrapper.setMethods({ login })
    
          const button = wrapper.find('#submit')
          button.trigger('click')
          await Vue.nextTick()
    
          expect(login).toHaveBeenCalled()
        } finally {
          wrapper.destroy()
        }
      })
    



  })