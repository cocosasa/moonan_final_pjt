
<template>
  <div>
    <div>
      <h1>QuestionDetailView</h1>
      <h1>{{ question?.title }}</h1>
      <p>{{ question?.content }}</p>
      <p>{{ question?.created_at }}</p>
      <p>{{ question?.updated_at }}</p>
      <p>{{ question?.points }}</p>
    </div>
    <div>
      <h3>조사하기</h3>
      <form>
        <input type="text" v-model="commentContent">
        <button @click.prevent="addComment">등록</button>
      </form>
    </div>
    <div>
      <h3>알려진 정보</h3>
      <CommentItem v-for="comment in question.question_comments" :key="comment" :comment-id="comment"/>
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
      question : null,
      commentContent : null,
    }
  },
  computed:{
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
        this.question = res.data
      })
      .catch((err) => {
        console.log(err)
      })
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
        this.getQuestionDetail()
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