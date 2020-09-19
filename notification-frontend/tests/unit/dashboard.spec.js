import { mount, shallowMount, createLocalVue } from '@vue/test-utils'

import Dashboard from '@/components/DashViews/Dashboard.vue'


describe('Dashboard', () => {

  test('Dashboard component render poperly', () => {
    const wrapper = shallowMount(Dashboard)

    expect(wrapper.find('.welcome-heading').text()).toEqual( 'Welcome Admin' );
    expect(wrapper.find('.welcome-info').text()).toEqual( 'Manage Website Notifications' );
  });

  });
