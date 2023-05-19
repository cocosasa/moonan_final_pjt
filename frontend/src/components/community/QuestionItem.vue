<template>
  <div class="question-item">
    <h3>{{ question.title }}</h3>
    <p>....내용....</p>
  </div>
</template>

<script>
export default {
  name:'QuestionItem',
  props : {
    question : Object,
  }
}
</script>

<style>
.question-item{
  height: 100px;
  width: 100%;
  background-color: whitesmoke;
}
</style>