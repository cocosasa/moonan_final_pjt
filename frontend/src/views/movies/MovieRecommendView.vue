<template>
  <div>
    <MovieRecommendList v-for="(recommendList, idx) in recommendLists" :key="idx" :recommendList="recommendList"/>
    <!-- <MovieRecommendList :recommendList="userRecommendList"/> -->
  </div>
</template>

<script>
import MovieRecommendList from '@/components/movies/MovieRecommendList.vue';
import _ from 'lodash'


export default {
  name:'MovieRecommendView',
  data(){
    return{
      recommendedMovieList : null,
    }
  },
  components : {
    MovieRecommendList,
  },
  computed: {
    recommendLists() {
      return _.sampleSize(this.$store.state.recommendLists, 3)
    }
  },
  methods:{
    // getUserRecommend(){
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/recommend/user/`,
    //   })
    //   .then((res) => {
    //     this.recommendedMovieList =res.data
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }
  }
}
</script>

<style>

</style>