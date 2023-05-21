<template>
  <div>
    <div class="my-4">
      <span class="fs-1">무비 몽타주</span>
      <div class="btn ms-5 btn-warning" @click="goToPostQuestion">질문하기</div>
    </div>
    <div>
      <QuestionItem v-for="q in questionList" :key="q.id" :question="q" />
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
    this.getQuestions()
  },
  computed:{
    questionList(){
      return this.$store.state.questionList
    }
  },
  methods:{
    getQuestions(){
      this.$store.dispatch('getQuestions')
    },
    goToPostQuestion(){
      this.$router.push({name: 'postquestion' })
    }
  }
}
</script>

<style>

</style>