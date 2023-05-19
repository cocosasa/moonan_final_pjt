<template>
  <div>
    <h1>" {{keyword}} " 검색결과</h1>
    {{ results }}
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'SearchView',
  components: {

  },
  created(){
    this.getSearchResults()
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
    getSearchResults(){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/movies/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
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