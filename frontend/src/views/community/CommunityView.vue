<template>
  <div>
    <div class="my-4">
      <span class="fs-1 bold">Movie Montage</span>
      <div class="btn ms-5 btn-warning bold" @click="goToPostQuestion">질문하기</div>
    </div>
    <div class="question-list">
      <QuestionItem v-for="q in questionList" :key="q.id" :question="q" />
      <div v-if="!questionList.length" class="text-center">
        더 이상 등록된 몽타주가 없습니다..
      </div>
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
    },
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  methods:{
    getQuestions(){
      this.$store.dispatch('getQuestions')
    },
    goToPostQuestion(){
      if(!this.isLogin){
        this.$store.dispatch('alertLogin')
        return
      }
      this.$router.push({name: 'postquestion' })
    }
  }
}
</script>

<style>
.question-list{
  min-width: 100%;
  min-height: 600px;
  padding: 10px;
  background-color: rgba(97, 97, 97, 0.411);
  border-radius: 5px;
  margin-bottom: 100px;
}
</style>