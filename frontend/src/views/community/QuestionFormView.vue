
<template>
  <div>
    <h1 class="mt-5">몽타주 등록</h1>
      <div class="AddWrap">
        <form>
          <table class="tbAdd">
            <colgroup>
              <col width="15%" />
              <col width="*" />
            </colgroup>
            <tr>
              <th>제목</th>
              <td><input type="text" v-model="title"/></td>
            </tr>
            <tr>
              <th>내용</th>
              <td><textarea v-model="content"></textarea></td>
            </tr>
            <tr>
              <th>이미지</th>
              <td>
                <input type="file" id="file">
              </td>
            </tr>
            <tr>
              <th>상금 ( 현재 {{ myPoints }}점 보유 )</th>
              <td>
                <input type="number" v-model="points"/>
              </td>
            </tr>
          </table>
        </form>
      </div>

      <div class="btnWrap">
        <a  @click="goToList" class="btnAdd btn">목록</a>
        <a  @click.prevent="addQuestion" class="btnAdd btn">등록</a>
      </div>	
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'QuestionFormView',
  data () {
    return {
      title : null,
      content : null,
      points : null,
      file : null
    }
  },
  computed:{
    myPoints(){
      return this.$store.getters.myPoints
    }
  },
  methods: {
    goToList(){
      this.$router.back()
    },
    addQuestion(){
      // var imagefile = document.getElementById('#file')
      const title = this.title
      const content = this.content
      const points = this.points
      var formdata = new FormData()
      formdata.append('title', title)
      formdata.append('content', content)
      formdata.append('points', points)
      // const file = document.getElementById('#file').files[0]
      // formdata.append('image', file)
      // const data = {
      //   title, content, points
      // }
      console.log(formdata)
      axios({
        method: 'post',
        url: `${API_URL}/community/questions/create/`,
        headers : {
          'Authorization' : `Token ${this.$store.state.token}`,
        },
        data : formdata,
      })
        .then((res) => {
          console.log(res.data)
          this.$router.push({name:'community'})
        })
        .catch((err) => {
          console.log(err)
        })
    }
    
  }
}
</script>

<style>
.tbAdd{border-top:1px solid #888;}
.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0;}
.tbAdd td{padding:10px 10px; box-sizing:border-box;}
.tbAdd td input{width:100%; min-height:30px; box-sizing:border-box; padding:0 10px;}
.tbAdd td textarea{width:100%; min-height:300px; padding:10px; box-sizing:border-box;}
.btnWrap{text-align:center; margin:20px 0 0 0;}
.btnWrap a{margin:0 10px;}
.btnAdd {background:#43b984}
.btnDelete{background:#f00;}
table{width:100%; border-collapse:collapse;}
.wrap{width:100%;}
.container{width:800px; margin:0 auto;}
</style>