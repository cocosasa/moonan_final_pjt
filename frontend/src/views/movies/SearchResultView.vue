<template>
  <div>
    <h1>" {{keyword}} " 검색결과</h1>
    <div v-if="!results">검색결과가 없습니다..</div>
    <div v-else class="row">
      <MovieCard v-for="movie in results" :key="movie.id" :movie="movie" @click.native="goToDetail(movie.id)"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  components: {
    MovieCard
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
      results : null,
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

<style></style>