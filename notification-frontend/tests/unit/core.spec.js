import { mount, shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import Vue from 'vue'
import Vuetify from 'vuetify'

import Footer from '@/components/core/Footer.vue'
import Drawer from '@/components/core/Drawer.vue'
import Toolbar from '@/components/core/Toolbar.vue'
// Store functionality
import actions from '@/store/actions'
import getters from '@/store/getters'
import modules from '@/store/modules'
import mutations from '@/store/mutations'
import state from '@/store/state'

const localVue = createLocalVue()
localVue.use(Vuex)

describe('Footer', () => {
  test('should render footer content correctly', () => {
    const wrapper = shallowMount(Footer)
    expect(wrapper.find('.copyright').text()).toEqual(
      'Admin Dashboard'
    );
  });

  });
