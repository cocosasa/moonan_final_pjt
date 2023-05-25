<template>
  <div class="comment">
    <div class="comment-item" :class="{ 'writer-comment': questionUser === commentUser, 'detective-comment': questionUser != commentUser }">
      <span>{{ commentUser }}</span>
      <p>{{ comment.content }}</p>
      <div v-if="myUserName=== commentUser && !isUpdating && isLogin">
        <button @click="initUpdate">수정</button>
        <button @click="deleteComment">삭제</button>
      </div>
      <button @click="initCcomment" v-if="!isCcommenting">대댓글 작성</button>
      <button v-if="questionUser != commentUser && myUserName!= commentUser && questionUser === myUserName && !question?.is_completed " @click="selectComment">채택하기</button>
      <!-- 수정폼 -->
      <form v-if="isUpdating" @submit.prevent="updateComment">
        <input type="text" v-model="formContent">
        <button>수정 완료</button>
      </form>
      <!-- 대댓글 폼 -->
      <form @submit.prevent="addCcomment" v-if="isCcommenting">
        <input type="text" v-model="formContent">
        <button >대댓글 달기</button>
      </form>
    </div>
    <CommentItem v-for="(child,idx) in comment.child_comments" :key="idx" :comment="child" :question-user="questionUser" class="ms-5 mt-3">
    </CommentItem>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'CommentItem',
  data(){
    return{
      user : null,
      isUpdating : false,
      isCcommenting : false,
      formContent : ''
    }
  },
  props:{
    comment : Object,
    questionUser : String,
  },
  created(){
    // this.getComment()
  },
  computed : {
    myUserName(){
      return this.$store.getters.myUserName
    },
    commentUser(){
      return this.comment?.user
    },
    question(){
      return this.$store.getters.question
    },
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  methods:{
    initUpdate() {
      this.isUpdating = true
      this.isCcommenting = false
    },
    initCcomment() {
      this.isUpdating = false
      this.isCcommenting = true
    },
    addCcomment() {
      const data = {
        content: this.formContent
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/questioncomments/${this.comment.id}/comments/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
        data: data,
      })
        .then((res) => {
          console.log(res.data)
          this.formContent = ''
          this.isCcommenting = false
          this.getQuestionDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateComment(){
      const data = {
        content: this.formContent
      }
      axios({
        method: 'put',
        url: `${API_URL}/community/questioncomments/${this.comment.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
        data: data,
      })
        .then((res) => {
          console.log(res.data)
          this.formContent = ''
          this.isUpdating = false
          this.getQuestionDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment(){
      axios({
        method: 'delete',
        url: `${API_URL}/community/questioncomments/${this.comment.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.getQuestionDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    selectComment(){
      // 'questions/correct/<int:question_pk>/<int:comment_pk>/
      axios({
        method: 'put',
        url: `${API_URL}/community/questions/correct/${ this.comment.question}/${ this.comment.id }/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res.data)
        this.getQuestionDetail()
      })
      .catch((err) => {
        console.log(err)
      })
    },
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
  }
}
</script>

<style>
.writer-comment{
  background-color: linen;
}
.detective-comment{
  background-color:aliceblue;
}
.comment-item{
  border-radius: 5px;
  padding: 10px;
  padding-right: 0;
}
.comment{
  border-radius: 5px;
  margin-top: 10px;
  /* padding: 10px;
  padding-right: 0; */
}
</style>