<template>
  <div>
    <MovieCard v-for="movie in movieList" :key="movie.id" :movie="movie"/>
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
  created() {
    this.getMovies()
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },

}
</script>

<style></style>