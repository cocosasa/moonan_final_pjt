
<template>
  <div>
    <hr>
    <div>
    <h1 class = 'bold'>&nbsp;&nbsp;Montage Interview</h1>
    <h5 @click="goToProfile" style = "text-align: right">의뢰자 {{ question?.user }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h5>
    </div>
    <hr>
    <div>
      <h1 style = "font-size: 50px">{{ question?.title }}</h1>
    </div>
    <br>
    <div>
      <img v-if="question.question_image" :src="`${BASE_URL}${question.question_image}`">
    <div>
      <h2>{{ question?.content }}</h2>
      <span style = "text-align: right">
        <h3 id = "hae" style = "color: green" v-if="question?.is_completed">해결됨&nbsp;&nbsp;&nbsp;&nbsp;</h3>
        <div>
        <h3 style = "color: red" v-if="!question?.is_completed">미해결&nbsp;&nbsp;&nbsp;&nbsp;</h3>
        <p v-if="!question?.is_completed"><span class="material-symbols-outlined">toll</span> 채택 시 {{ question?.points }} 포인트 획득&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        </div>
      </span>
    </div>
      <hr>
      <p>작성 시각 : {{ createdAt }}</p>
      <p>최종 수정 시각 : {{ updatedAt }}</p>

    </div>
    <div v-if="myUserName === question?.user">
      <button class = "edit-delete bold"><span class="material-symbols-outlined">edit</span> 수정하기</button>
      <button class = "edit-delete bold" @click="deleteQuestion"><span class="material-symbols-outlined">delete</span> 삭제하기</button>
    </div>
    <hr>
    <div>
      <h3 class = "bold" v-if="myUserName != question?.user">도움 주기</h3>
      <h3 class = "bold" v-if="myUserName === question?.user">정보 추가</h3>
      <form>
        <input type="text" v-model="commentContent" class="form-text p-2 rounded-1">&nbsp;&nbsp;
        <button @click.prevent="addComment" class="btn btn-light bold">등록</button>
      </form>
    </div>
    <div class="my-3">
      <h3 class = "bold">알려진 정보</h3>
      <CommentItem v-for="comment in question?.question_comments" :key="comment.id" :comment="comment" :question-user="question?.user"/>
      <br>
      <div style = "text-align: center" v-if="question?.question_comments">
        <span>추가 내용이 없습니다..</span>
      </div>
    </div>
  </div>
</template>

<script>
import CommentItem from '@/components/community/CommentItem.vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'
export default {
  name : 'QuestionDetailView',
  components:{
    CommentItem,
  },
  created(){
    this.getQuestionDetail()
  },
  data(){
    return {
      commentContent : null,
    }
  },
  computed:{
    question(){
      return this.$store.getters.question
    },
    myUserName(){
      return this.$store.state.username
    },
    createdAt(){
      const time = new Date(this.question?.created_at)
      return time.toLocaleDateString() + time.toLocaleTimeString()
    },
    updatedAt(){
      const time = new Date(this.question?.updated_at)
      return time.toLocaleDateString() + time.toLocaleTimeString()
    },
    BASE_URL(){
      return 'http://127.0.0.1:8000'
    },
    myToken(){
      return this.$store.state.token
    }
  },
  methods :{
    getQuestionDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/community/questions/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.myToken}`
        }
      })
      .then((res) => {
        console.log(res.data)
        this.$store.dispatch('changeQuestionData', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToProfile(){
      this.$router.push({name:'profile', params:{username: this.question?.user }})
    },
    addComment(){
      if(!this.myToken){
        this.$store.dispatch('AlertLogin')
        return
      }
      const data = {
        content : this.commentContent
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/questions/${this.$route.params.id}/comments/`,
        headers: {
          'Authorization': `Token ${this.myToken}`,
        },
        data: data,
      })
      .then((res) => {
        console.log(res.data)
        this.commentContent = ''
        this.getQuestionDetail()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteQuestion(){
      axios({
        method: 'delete',
        url: `${API_URL}/community/questions/${this.$route.params.id}/`,
        headers: {
          'Authorization': `Token ${this.myToken}`,
        },
      })
      .then((res) => {
        console.log(res.data)
        alert('질문이 삭제되었습니다')
        this.$router.push({ name: 'community' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}
.edit-delete {
  border: solid 1px black;
}

</style>