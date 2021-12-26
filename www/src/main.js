// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueParticles from 'vue-particles'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import VueResource from 'vue-resource'
import store from './store'
import { Button } from 'ant-design-vue'

Vue.use(VueParticles)
Vue.use(ElementUI)
Vue.use(axios)
Vue.use(VueResource)
Vue.use(Button)

Vue.config.productionTip = false
Vue.http.options.emulateJSON = true
// Vue.prototype.$http = axios
// axios.defaults.baseURL = '/api'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
Vue.http.headers.common['token'] = sessionStorage['token']
// Vue.http.interceptors.push((request, next) => {
//   request.credentials = true; // 接口每次请求会跨域携带cookie
//   // request.method= 'POST'; // 请求方式（get,post）
//   // request.headers.set('token', localStorage.getItem('Authorization')) // 请求headers携带参数
//   request.headers.set('Authorization', localStorage.getItem('Authorization')) // 请求headers携带参数
//   console.log('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', localStorage.getItem('Authorization'))
//   next(function(response) {
//     return response
//   })
// })
