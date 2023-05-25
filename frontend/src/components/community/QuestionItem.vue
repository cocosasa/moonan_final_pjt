<template>
    <div class="question-item d-flex justify-content-between bold" style = "color: black" @click="goToQuestionDetail(question)">
      <div class="w-75">
        <br>
        <h3 class="mb-4">{{ question.title }}</h3>
        <hr>
        <p>{{ question.user }}의 질문</p>
        <!-- <p>{{ shortenContent }}</p> -->
      </div>
      <div class="my-auto">
        <div class="point-box" v-if="!question?.is_completed"> {{ question.points }} Point</div>
        <span style = "text-align: right">
          <h3 style = "color: green" v-if="question?.is_completed">해결됨&nbsp;&nbsp;&nbsp;&nbsp;</h3>
        </span>
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
  border-radius: 5px;
  padding: 10px;
  border: solid 2px;
}
.completed-item{
  height: 150px;
  width: 100%;
  background-color: whitesmoke;
  overflow: hidden;
  margin-bottom: 20px;
  border-radius: 5px;
  padding: 10px;
  border: solid 2px;
}
.point-box{
  width: 150px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  word-wrap: break-word;
  background-color: #ffd35a;
  border-radius: 10px;
  border: solid 3px
}
</style>