<template>
  <div>
    <div class="img-1"></div>
    <MovieRecommendList v-for="(recommendList, idx) in recommendLists" :key="idx" :recommendList="recommendList"/>

  </div>
</template>

<script>
import MovieRecommendList from '@/components/movies/MovieRecommendList'

export default {
  name : 'MainView',
  components : {
    MovieRecommendList,
  },
  created() {
    this.getMovies()
  },
  data () {
    return {

    }
  },
  computed :{
    movieList (){
      return this.$store.state.movieList
    },
    recommendLists() {
      return this.$store.state.recommendLists
    }
  },
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },

}
</script>

<style>
.img-1 {
  width: 1200px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset 96px 50px 250px 29px #000, inset -54px -50px 250px 20px #000;
  background: url('@/assets/img.bmp') no-repeat center;
  background-size: cover;
}
</style>