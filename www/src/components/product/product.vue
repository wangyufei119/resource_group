<template>
  <div>
      <div>
        <a-button type="primary" @click.native="get_user_prodct">当前可用产品</a-button>
        <span v-for="prodcut in product_list" v-bind:key="prodcut.id">
           {{prodcut.name}}&nbsp;&nbsp;&nbsp;&nbsp;
        </span>
      </div>
      <!-- <div>
        <a-button type="primary" @click.native="get_group_list">所有资源组列表</a-button>
        <span v-for="data in all_group_data" v-bind:key="data.id">
           {{data.name}}&nbsp;&nbsp;&nbsp;&nbsp;
        </span>
      </div>

      <div>
        <a-button type="primary" @click.native="get_all_user">获取所有用户</a-button>
        <span v-for="user in all_user_list" v-bind:key="user.id">
           {{user.username}}&nbsp;&nbsp;&nbsp;&nbsp;
        </span>
      </div>

      <div>
        <a-button type="primary" @click.native="group_add">添加资源组</a-button>
      </div>

      <el-form>
        <el-form-item>
          <el-input placeholder="资源组" v-model="group_name"></el-input>
        </el-form-item>

        <el-form-item>
          <el-input placeholder="用户" v-model="username"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary"  @click.native="group_user_add">添加用户到资源组</el-button>
        </el-form-item>
    </el-form> -->
  </div>
</template>
<script>

export default {
  data () {
    return {
      product_list: [],
      all_product_list: [],
      all_user_list: [],
      group_name: '',
      username: ''
    }
  },
  // 页面加载后执行
  mounted: function () {
  },
  methods: {
    get_user_prodct () {
      var data = {}
      data.username = 'admin'
      this.$http.get('api/group/group_user_product/list', {'params': data}, {'Content-Type': 'application/json'}).then((res) => {
        console.log(res.data)
        if (res.data['status'] === 1) {
          this.product_list = res.data['result']
        } else {
          alert('暂无数据')
        }
      })
    },

    get_group_list () {
      var data = {}
      this.$http.get('api/group/group/list', {'params': data}, {'Content-Type': 'application/json'}).then((res) => {
        console.log(res.data)
        if (res.data['status'] === 1) {
          this.all_group_data = res.data['result']
        } else {
          alert('暂无数据')
        }
      })
    },

    get_all_user () {
      var data = {}
      this.$http.get('api/account/all', {'params': data}, {'Content-Type': 'application/json'}).then((res) => {
        console.log(res.data)
        if (res.data['status'] === 1) {
          this.all_user_list = res.data['result']
        } else {
          alert('暂无数据')
        }
      })
    },

    group_add () {
      // 当前页面打开
      // this.$router.push({path: '/group_add'})
      // 打开新窗口
      let routeUrl = this.$router.resolve({
        path: "/group_add"
      })
      window.open(routeUrl.href, '_blank')
    },

    group_user_add () {
      var data = {}
      data.group_name = this.group_name
      data.user_name = this.username
      // this.$http.headers.common['token'] = sessionStorage['token']
      this.$http.post('/api/group/group_user/update', data).then((res) => {
        console.log(res.data)
        if (res.data['status'] === 1) {
          alert('更新数据成功')
          this.group_name = ''
          this.username = ''
        } else {
          alert('更新数据失败')
        }
      })
    }
  }
}
</script>
<style scoped>

</style>
