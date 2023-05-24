
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
                <input @change="inputImage" ref="questionImage" type="file" id="file">
              </td>
            </tr>
            <tr>
              <th>상금 ( 현재 {{ myUserData.points  }}점 보유 )</th>
              <td>
                <input type="number" v-model="points" min="0" />
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
      points : 0,
      file : null
    }
  },
  computed:{
    myUserData(){
      return this.$store.getters.myUserData
    }
  },
  methods: {
    goToList(){
      this.$router.back()
    },
    inputImage(){
      console.log(this.file)
      this.file = this.$refs.questionImage.files[0]
    },
    addQuestion(){
      const title = this.title
      const content = this.content
      const points = this.points
      if(points<0){
        alert('상금은 0 이상이어야 합니다!')
        return
      }
      else if(points> this.myUserData.points ){
        alert('보유포인트 만큼만 사용할 수 있습니다.')
        return
      }
      var formdata = new FormData()
      formdata.append('title', title)
      formdata.append('content', content)
      formdata.append('points', points)
      let headers = ''
      if(this.file){
        formdata.append('question_image', this.file)
        headers =  {
          'Authorization' : `Token ${this.$store.state.token}`,
          'Content-Type' : 'multipart/form-data'
        }
      }
      else{
        headers = {
          'Authorization': `Token ${this.$store.state.token}`,
        }
      }
      console.log(formdata)
      axios({
        method: 'post',
        url: `${API_URL}/community/questions/create/`,
        headers,
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