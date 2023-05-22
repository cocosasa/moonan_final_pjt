<template>
  <div>
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
  },
  created(){
    this.getComment()
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

</style>