import { mount, shallowMount, createLocalVue } from '@vue/test-utils'
import Vuetify from 'vuetify';
import Vue from 'vue';
import Notifications from '@/components/NotificationViews/Notifications.vue'

describe('Notifications', () => {

    it("notification table header contains event and notification_text", () => {
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications
            }
        })
        expect(wrapper.vm.headers).toEqual([
            { text: 'Event',align: 'left', value: 'event' },
            { text: 'Text', value: 'notification_text' },
            { text: 'Actions', value: 'name', sortable: false }
        ]);
      });


        it('it should render notifications list correctly', async () => {
            const notification_list = [{
                event: 'first-visit',
                notification_text: 'my notification text'
                }]
                const fetchNotifications = jest.fn()
                const wrapper = mount(Notifications, {
                    methods: {
                        fetchNotifications: fetchNotifications
                    }
                })
            try {
                await wrapper.setData({ notifications: notification_list })
                expect(wrapper.html()).toContain('my notification text')
    
            } finally {
              wrapper.destroy()
            }
          })

          
      it('it should open new notification creation dialog when click on new notification button', async () => {
    
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications
            }
        })
        try {
            // await wrapper.setData({ dialog: true })
            wrapper.find('button#newNotification').trigger('click')
            await wrapper.vm.$nextTick()
            expect(wrapper.find('#submitButton').isVisible()).toBe(true)

        } finally {
        wrapper.destroy()
        }
      })


      it('it should set default data to new notification creation input form', async () => {
    
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications
            }
        })
        try {
            await wrapper.setData({ 
                notification: {
                event: '1st-visit',
                notification_text: 'Hello user'
                } })
            
            wrapper.find('button#newNotification').trigger('click')
            await wrapper.vm.$nextTick()

            const notification_text = wrapper.find('#notification_text').element.value
            expect(notification_text).toBe('Hello user')

        } finally {
        wrapper.destroy()
        }
      })


      it('submit button should disabled when notification_text field is empty', async () => {
    
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications
            }
        })
        try {
            await wrapper.setData({ 
                notification: {
                event: '1st-visit',
                notification_text: ''
                } })
            
            wrapper.find('button#newNotification').trigger('click')
            await wrapper.vm.$nextTick()

            const button = wrapper.find('#submitButton')
            await wrapper.vm.$nextTick()
            expect(button.attributes().disabled).toBe('disabled')

        } finally {
        wrapper.destroy()
        }
      })



      it('it should call save method when click on save button', async () => {
        const save = jest.fn()
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications,
                save: save
            }
        })
        try {
            await wrapper.setData({ 
                notification: {
                event: '1st-visit',
                notification_text: 'Dear User'
                } })
            
            wrapper.find('button#newNotification').trigger('click')
            await wrapper.vm.$nextTick()

            wrapper.find('#submitButton').trigger('click')
            await wrapper.vm.$nextTick()
            
            
            expect(save).toHaveBeenCalled()

        } finally {
        wrapper.destroy()
        }
      })




      it('it should call close method when click on cancel button', async () => {
        const close = jest.fn()
        const fetchNotifications = jest.fn()
        const wrapper = mount(Notifications, {
            methods: {
                fetchNotifications: fetchNotifications,
                close: close
            }
        })
        try {
            await wrapper.setData({ 
                notification: {
                event: '1st-visit',
                notification_text: 'Dear User'
                } })
            
            wrapper.find('button#newNotification').trigger('click')
            await wrapper.vm.$nextTick()

            wrapper.find('#cancelButton').trigger('click')
            await wrapper.vm.$nextTick()
            
            
            expect(close).toHaveBeenCalled()

        } finally {
        wrapper.destroy()
        }
      })





  })