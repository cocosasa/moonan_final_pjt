<template>
  <div>
    영화 정보
    <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="">
    <div class="card-body">
        <h5 class="card-title">{{ movie?.title }}</h5>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
  },
  created(){
    this.getMovieDetail()
  },
  data() {
    return {
      movie : null,
    }
  },
  computed: {

  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },

}
</script>

<style>

</style>