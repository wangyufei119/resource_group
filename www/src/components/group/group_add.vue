<template>
  <div>
    <el-form>
      <el-form-item>
        <el-input placeholder="资源组明" v-model="name"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary"  @click.native="group_add">添加</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data () {
    return {
      name: ''
    }
  },
  mounted: function () {
  },
  methods: {
    group_add () {
      var data = {}
      data.name = this.name
      this.$http.headers.common['token'] = sessionStorage['token']
      this.$http.post('/api/group/group/add', data).then((res) => {
        console.log(res.data)
        if (res.data['status'] === 1) {
          alert('新增资源组成功')
        } else {
          alert('暂无数据')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
