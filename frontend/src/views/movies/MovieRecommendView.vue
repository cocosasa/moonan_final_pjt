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
      return [
        this.$store.state.popularMovieList.slice(10, 16),
        this.$store.state.popularMovieList.slice(20, 26),
        this.$store.state.popularMovieList.slice(120, 126),
      ]
    }
  },
  methods:{
    
  }
}
</script>

<style>

</style>