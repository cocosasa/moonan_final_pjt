<template>
  <div class="search-view">
    <div class="my-5">
      <h1>" {{keyword}} " 검색결과</h1>
    </div>
    <div  class="ms-5" v-if="!results?.length">검색된 결과가 없습니다..</div>
    <MovieList :movie-list="results"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieList.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchResultView',
  components: {
    MovieList
  },
  created(){
    this.getSearchResults(this.keyword)
  },
  beforeRouteUpdate(to, from, next) {
    this.getSearchResults(to.params.keyword)
    next()
  },
  data() {
    return {
      results : [],
    }
  },
  computed: {
    keyword(){
      return this.$route.params.keyword
    }
  },
  methods: {
    getSearchResults(keyword){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/movies/${keyword}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.results = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },

}
</script>

<style>
.search-view{
  min-height: 1000px;
}
</style>