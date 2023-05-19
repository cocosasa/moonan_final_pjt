<template>
  <div>
    <div>
      <h2>영화 몽타주</h2>
      <button>질문하기</button>
    </div>
    <div>
      <QuestionItem v-for="q in questionList" :key="q.id" :question="q"/>
    </div>
  </div>
</template>

<script>
import QuestionItem from '@/components/community/QuestionItem.vue';
export default {
  name:'CommunityView',
  components:{
    QuestionItem,
  },
  created(){
    this.getQuestionList()
  },
  computed:{
    questionList(){
      return this.$store.state.questionList
    }
  },
  methods:{
    getQuestionList(){
      this.$store.dispatch('getQuestionList')
    }
  }
}
</script>

<style>

</style>