<template>
  <div>
    Main
    <MovieRecommendList/>
    <!-- {{ movieList }} -->
  </div>
</template>

<script>
import MovieRecommendList from './MovieRecommendList'
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
      // movieList : null,
    }
  },
  computed :{
    movieList (){
      return this.$store.state.movieList
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

</style>