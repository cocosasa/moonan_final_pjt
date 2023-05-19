<template>
  <div>
    Movie
    <MovieList/>
    <!-- {{ movieList }} -->
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  created() {
    this.getMovies()
  },
  data() {
    return {
      // movieList : null,
    }
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