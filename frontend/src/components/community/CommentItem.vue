<template>
  <div class="comment" :class="{'writer-comment': questionUser===comment.user, 'detective-comment': questionUser != comment.user }">
    <span>{{ comment.user }}</span>
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'CommentItem',
  data(){
    return{
      comment : null,
      user : null
    }
  },
  props:{
    commentId : Number,
    questionUser : String,
  },
  created(){
    this.getComment()
  },
  computed : {
  },
  methods:{
    getComment(){
      axios({
        method: 'get',
        url: `${API_URL}/community/questioncomments/${this.commentId}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.comment = res.data
        })
        .then(()=>{
        //   axios({
        //     method: 'get',
        //     url: `${API_URL}/community/questioncomments/${this.commentId}/`,
        //   })
        //     .then((res) => {
        //       console.log(res.data)
        //       this.comment = res.data
        //     })
        //     .catch((err) => {
        //       console.log(err)
        //     })
        // })
        // .catch((err) => {
        //   console.log(err)
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
.comment{
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
}
</style>