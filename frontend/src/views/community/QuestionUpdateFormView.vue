
<template>
  <div>
    <h1 class="mt-5">몽타주 수정</h1>
      <div class="AddWrap">
        <form>
          <table class="tbAdd">
            <colgroup>
              <col width="15%" />
              <col width="*" />
            </colgroup>
            <tr>
              <th>제목</th>
              <td><input type="text" @change="changeTitle" :value="question?.title"/></td>
            </tr>
            <tr>
              <th>내용</th>
              <td><textarea @change="changeContent" :value="question?.content" ></textarea></td>
            </tr>
            <tr>
              <th>이미지</th>
              <td>
                <input @change="inputImage" ref="questionImage" type="file" id="file" :value="question.image_path">
              </td>
            </tr>
          </table>
        </form>
      </div>

      <div class="btnWrap">
        <a  @click="goToList" class="btnAdd btn">목록</a>
        <a  @click.prevent="updateQuestion" class="btnAdd btn">수정</a>
      </div>	
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'QuestionUpdateFormView',
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
    },
    question(){
      return this.$store.getters.question
    }
  },
  methods: {
    goToList(){
      this.$router.back()
    },
    changeTitle(e){
      this.title = e.target.value
    },
    changeContent(e){
      this.content = e.target.value
    },
    inputImage(){
      this.file = this.$refs.questionImage.files[0]
      console.log(this.file)
    },
    updateQuestion(){
      if(!this.title){
        this.title = this.question.title
      }
      if(!this.content){
        this.content = this.question.content
      }
      const title = this.title
      const content = this.content
      const points = 0
  
      var formdata = new FormData()
      formdata.append('title', title)
      formdata.append('content', content)
      formdata.append('points', points)
      let headers = ''
      if(this.file){
        formdata.append('question_image', this.file)
        headers =  {
          'Authorization' : `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data'
        }
      }
      else{
        alert('이미지를 선택해 주세요')
        return
      }
      console.log(formdata)
      axios({
        method: 'put',
        url: `${API_URL}/community/questions/${this.question.id}/`,
        headers,
        data : formdata,
      })
        .then((res) => {
          console.log(res.data)
          this.$router.back()
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