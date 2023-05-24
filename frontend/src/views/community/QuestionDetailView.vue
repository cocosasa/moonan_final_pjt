
<template>
  <div>
    <div>
      <h1>Montage Interview</h1>
      <h1>제목{{ question?.title }}</h1>
      <h1 @click="goToProfile">목격자 {{ question?.user }}</h1>
      <img v-if="question.question_image" :src="`${BASE_URL}${question.question_image}`">
      <p>증언 {{ question?.content }}</p>
      <p>만들어진 시각 :{{ createdAt }}</p>
      <p>수정된 시각 : {{ updatedAt }}</p>
      <p>{{ question?.points }}</p>
      <h3 v-if="question?.is_completed">해결됨</h3>
      <h3 v-if="!question?.is_completed">미해결</h3>
    </div>
    <div v-if="myUserName === question?.user">
      <button>수정</button>
      <button @click="deleteQuestion">삭제</button>
    </div>
    <div>
      <h3 v-if="myUserName != question?.user">조사하기</h3>
      <h3 v-if="myUserName === question?.user">추가 증언하기</h3>
      <form>
        <input type="text" v-model="commentContent" class="form-text p-2 rounded-1">
        <button @click.prevent="addComment" class="btn btn-danger">등록</button>
      </form>
    </div>
    <div class="my-3" v-if="question">
      <h3>알려진 정보</h3>
      <CommentItem v-for="comment in question?.question_comments" :key="comment.id" :comment="comment" :question-user="question?.user"/>
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
    }
  },
  methods :{
    getQuestionDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/community/questions/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
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
      const data = {
        content : this.commentContent
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/questions/${this.$route.params.id}/comments/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
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
          'Authorization': `Token ${this.$store.state.token}`,
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

</style>