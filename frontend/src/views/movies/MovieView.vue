<template>
  <div class="infinite">
    Movie
    <div>카테고리</div>
    <div class="container">
      <MovieList :movie-list="loadedMovieList"/>
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">목록의 끝입니다 :)</div>
      </infinite-loading>
    </div>
    <!-- {{ movieList }} -->
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';
import MovieList from '@/components/movies/MovieList'
export default {
  name: 'MovieView',
  components: {
    MovieList,
    InfiniteLoading
  },
  created() {
    if( !this.$store.state.movieList){
      this.getMovies()
    }
  },
  data() {
    return {
      loadedMovieList : [],
      currentPage : 1,
    }
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    },
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    infiniteHandler($state) {

      setTimeout(() => {
        if (this.currentPage < 10) {
          $state.loaded()
          this.currentPage += 1
          this.loadedMovieList = this.$store.state.movieList.slice(0, 20 * this.currentPage)
        } else {
          // 끝 지정(No more data)
          $state.complete()
        }
      }, 0)}
  }
}
</script>

<style>
  /* .infinite{

  } */
</style>