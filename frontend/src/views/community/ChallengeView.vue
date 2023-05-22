<template>
  <div>
    <h1>Challenge</h1>
    <QuizItem :movie="randomMovie"/>
  </div>
</template>

<script>
import QuizItem from '@/components/community/QuizItem.vue'
export default {
  name :'ChallengeView',
  components : {
    QuizItem,
  },
  computed:{
    randomMovie () {
      return this.$store.state.popularMovieList.slice(40,41)[0]
    }
  }

}
</script>

<style>

</style>