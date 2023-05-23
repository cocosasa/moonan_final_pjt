<template>
  <div>
    <CategoryComponent @search-genre="searchGenre"/>
    <div class="">
      <div class="d-flex">
        <div class="ms-auto me-2" :class="{'text-danger': sortBy === 1 }" @click="sortByPopular">인기 순</div> | 
        <div class="ms-2" :class="{ 'text-danger': sortBy === 2 }" @click="sortByVoteAvg">평점 순</div>
      </div>
      <MovieList v-if="!isGenreSearch && sortBy===1" :movie-list="loadedPopularMovieList"/>
      <MovieList v-if="!isGenreSearch &&  sortBy===2" :movie-list="loadedVoteAvgMovieList"/>
      <MovieList v-if="isGenreSearch" :movie-list="genreSearchMovieList"/>
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
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

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
      genreSearchMovieList : [],
      selectedGenres: [],
      currentPage : 1,
      sortBy : 1,
      isGenreSearch : false,
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
      this.getGenreAxios()
    },
    sortByVoteAvg(){
      this.sortBy = 2
      this.getGenreAxios()
    },
    getGenreAxios(){
      if (!this.selectedGenres.length) {
        this.isGenreSearch = false
      }
      else {
        const keywords = this.selectedGenres.join(' ')
        console.log(keywords)
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/search/movies/genres/${keywords}/${this.sortBy}/`,
        })
          .then(res => {
            console.log(res.data)
            this.genreSearchMovieList = res.data
            this.isGenreSearch = true
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    searchGenre(selectedGenreList){
      this.selectedGenres = selectedGenreList
      this.getGenreAxios()
    }
  }
}
</script>

<style>

</style>