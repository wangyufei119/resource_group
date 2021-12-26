import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import 'element-ui/lib/theme-chalk/index.css'
import Login from '@/components/login/Login'
import Group from '@/components/group/Group'
import GroupAdd from '@/components/group/group_add'
import Product from '@/components/product/product'

Vue.use(Router)
Vue.use(Element)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/group/',
      name: 'Group',
      component: Group
    },
    {
      path: '/group_add/',
      name: 'GroupAdd',
      component: GroupAdd
    },
    {
      path: '/product/',
      name: 'Product',
      component: Product
    }
  ]
})
