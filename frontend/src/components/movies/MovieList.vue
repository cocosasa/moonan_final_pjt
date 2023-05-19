<template>
  <div class="row">
    <MovieCard v-for="movie in movieList" :key="movie.id" :movie="movie" @click.native="goToDetail(movie)"/>
  </div>
</template>

<script>
import MovieCard from './MovieCard.vue'
export default {
  name: 'MovieList',
  components: {
    MovieCard
  },

  data() {
    return {
      
    }
  },
  props:{
    movieList: Array,
  },
  created() {
  },
  computed: {
  },
  methods: {
    goToDetail(movie){
      this.$router.push({name:'detail', params:{id:movie.id}})
    },
  },

}
</script>

<style>

</style>