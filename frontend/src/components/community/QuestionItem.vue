<template>
  <div class="question-item d-flex justify-content-between">
    <div>
      <h3 class="mb-4" @click="goToQuestionDetail(question)">{{ question.title }}</h3>
      <p>{{ question.user }}</p>
      <p>{{ shortenContent }}</p>
    </div>
    <div class="my-auto">
      <div class="point-box"> {{ question.points }} Point</div>
    </div>
  </div>
</template>

<script>
export default {
  name:'QuestionItem',
  props : {
    question : Object,
  },
  computed : {
    shortenContent(){
      let content = this.question.content

      if (content.length > 30) {
        return content.substring(0, 30) + '...'
      } else {
        return content
      }
    }
  },
  methods:{
    goToQuestionDetail(question){
      this.$router.push({name:'questiondetail', params:{ id : question.id}})
    }
  }
}
</script>

<style>
.question-item{
  height: 150px;
  width: 100%;
  background-color: whitesmoke;
  overflow: hidden;
  margin-bottom: 20px;
  border-radius: 10px;
  padding: 10px;
}
.point-box{
  width: 150px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  word-wrap: break-word;
  background-color: white;
  border-radius: 10px;
}
</style>