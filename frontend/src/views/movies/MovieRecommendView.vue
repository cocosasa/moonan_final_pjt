<template>
  <div>
    <MovieRecommendList v-for="(recommendList, idx) in recommendLists" :key="idx" :recommendList="recommendList"/>
  </div>
</template>

<script>
import MovieRecommendList from '@/components/movies/MovieRecommendList.vue';

export default {
  name:'MovieRecommendView',
  components : {
    MovieRecommendList,
  },
  computed: {
    recommendLists() {
      return this.$store.state.recommendLists
    }
  },
}
</script>

<style>

</style>