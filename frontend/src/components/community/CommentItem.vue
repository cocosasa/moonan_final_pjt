<template>
  <div class="comment">
    <div class="comment-item" :class="{ 'writer-comment': questionUser === commentUser, 'detective-comment': questionUser != commentUser }">
      <span>{{ commentUser }}</span>
      <p>{{ comment.content }}</p>
      <div v-if="myUserName=== commentUser && !isUpdating">
        <button @click="initUpdate">수정</button>
        <button>삭제</button>
      </div>
      <button @click="initCcomment" v-if="!isCcommenting">대댓글 작성</button>
      <button v-if="questionUser != commentUser && myUserName!= commentUser && questionUser === myUserName">채택하기</button>
      <!-- 수정폼 -->
      <form v-if="isUpdating">
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
        })
        .catch((err) => {
          console.log(err)
        })
    }
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