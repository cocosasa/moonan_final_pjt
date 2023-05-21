<template>
  <div>
    <div class="d-flex">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="movie-detail-img">
      <div class="ms-5">
        <div>
          <span class="">{{ movie?.title }}</span>
        </div>
        <div>
          <span>개봉일 : {{ movie?.released_date }}</span>
          <p>별{{ movie?.vote_avg }} 점</p>
          <p>{{ movie?.genres }}</p>
        </div>
        <div>
          <div>보고싶어요 토글</div>
          <div>Watched 토글</div>
        </div>
      </div>
    </div>
    <div>
      <p>줄거리</p>
      <p>{{ movie?.overview }}</p>
    </div>
    <div>
      <h3>출연 배우</h3>
      <div class="d-flex row">
        <ActorItem/>
        <ActorItem/>
        <ActorItem/>
      </div>
    </div>
    <div>
      <h3>한줄평</h3>
      
    </div>
  </div>
</template>

<script>
import ActorItem from '@/components/movies/ActorItem.vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    ActorItem,
  },
  created(){
    this.getMovieDetail()
    this.getMovieActors()
  },
  data() {
    return {
      movie : null,
    }
  },
  computed: {
    shorten() {
      let overview = this.movie.overview

      if (overview.length > 40) {
        return overview.substring(0, 40) + '...'
      } else {
        return overview
      }
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${this.$route.params.id}/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`
        // }
      })
        .then((res) => {
          console.log(res.data)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieActors(){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${this.$route.params.id}/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`
        // }
      })
      .then((res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },

}
</script>

<style>
.movie-detail-img {
  width: 400px;
}
</style>