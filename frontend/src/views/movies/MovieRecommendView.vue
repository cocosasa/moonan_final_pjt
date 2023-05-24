<template>
  <div>
    <MovieRecommendList v-for="(recommendList, idx) in recommendLists" :key="idx" :recommendList="recommendList"/>
  </div>
</template>

<script>
import MovieRecommendList from '@/components/movies/MovieRecommendList.vue';
import _ from 'lodash'


export default {
  name:'MovieRecommendView',
  components : {
    MovieRecommendList,
  },
  computed: {
    recommendLists() {
      return _.sampleSize(this.$store.state.recommendLists, 3)
    }
  },
  methods:{
    
  }
}
</script>

<style>

</style>