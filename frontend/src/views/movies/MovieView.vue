<template>
  <div>
    <div>카테고리</div>
    <CategoryComponent/>
    <div class="">
      <div class="d-flex">
        <div class="ms-auto me-2" :class="{'text-danger': sortBy === 1 }" @click="sortByPopular">인기 순</div> | 
        <div class="ms-2" :class="{ 'text-danger': sortBy === 2 }" @click="sortByVoteAvg">평점 순</div>
      </div>
      <MovieList v-if="sortBy===1" :movie-list="loadedPopularMovieList"/>
      <MovieList v-if="sortBy===2" :movie-list="loadedVoteAvgMovieList"/>
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">더 이상 영화가 없습니다 :D</div>
      </infinite-loading>
    </div>
    <!-- {{ movieList }} -->
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';
import CategoryComponent from '@/components/movies/CategoryComponent.vue';
import MovieList from '@/components/movies/MovieList'
export default {
  name: 'MovieView',
  components: {
    InfiniteLoading,
    CategoryComponent,
    MovieList,
  },
  created() {
    if(!this.$store.popularMovieList){
      this.getMovies()
    }
  },
  data() {
    return {
      loadedPopularMovieList : [],
      loadedVoteAvgMovieList : [],
      currentPage : 1,
      sortBy : 1,
    }
  },
  computed: {
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getGenres')
    },
    infiniteHandler($state) {
      setTimeout(() => {
        if (this.currentPage < 10) {
          $state.loaded()
          this.currentPage += 1
          this.loadedPopularMovieList = this.$store.state.popularMovieList.slice(0, 20 * this.currentPage)
          this.loadedVoteAvgMovieList = this.$store.state.voteAvgMovieList.slice(0, 20 * this.currentPage)
        } else {
          // 끝 지정(No more data)
          $state.complete()
        }
      }, 100)
    },
    sortByPopular(){
      this.sortBy = 1
    },
    sortByVoteAvg(){
      this.sortBy = 2
    },
  }
}
</script>

<style>

</style>