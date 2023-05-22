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
        <div class="d-flex">
          <div @click="toggleWant">
            <button :class="{'btn-secondary':!isWanted, 'btn-primary':isWanted}" class="btn"> 보고 싶어요 </button>
          </div>
          <div @click="toggleWatch">
            <button :class="{'btn-secondary': !isWatched, 'btn-primary':isWatched }" class="btn">봤어요</button>
          </div>
        </div>
      </div>
    </div>
    <!-- <MovieVideo :movie="movie.title"/> -->
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
      <h3>한 줄평 쓰기</h3>
      <div>
        <form name="reviewform" id="reviewform">
          <input type="text" v-model="reviewContent">
          <StarScore @set-score="setScore"/>
          {{ reviewScore }} 점

          <button @click.prevent="addReview"> 등록하기 </button>
        </form>
      </div>
      <h3>한 줄평</h3>
      <div>
        <ReviewItem v-for="(review,idx) in reviews" :key="idx" :review="review"/>
      </div>
    </div>
  </div>
</template>

<script>
import ActorItem from '@/components/movies/ActorItem.vue';
// import MovieVideo from '@/components/movies/MovieVideo.vue';
import ReviewItem from '@/components/community/ReviewItem.vue';
import StarScore from '@/components/community/StarScore.vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    ActorItem,
    // MovieVideo,
    StarScore,
    ReviewItem,
  },
  created(){
    this.getMovieDetail()
    this.getMovieActors()
    this.getMovieReviews()
    this.getProfile()
  },
  data() {
    return {
      movie : null,
      reviews : null,
      reviewContent : null,
      reviewScore : 0.5,
      isWatched : false,
      isWanted : false,
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
    getProfile(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$store.state.username}/`,
      })
      .then(res => {
        console.log(res.data)
        console.log(this.$route.params.id)
        if (res.data.want_to_see_movies.includes(this.$route.params.id)){
          this.isWanted = true
        }
        if (res.data.watched_movies.includes(this.$route.params.id))
          this.isWatched = true
      })
      .catch(err => {
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
    },
    getMovieReviews(){
      axios({
        method: 'get',
        url: `${API_URL}/community/reviews/`,
      })
      .then((res) => {
        console.log(res.data)
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    addReview(){
      const content = this.reviewContent
      const score = this.reviewScore
      var formdata = new FormData()
      formdata.append('content', content)
      formdata.append('score', score)

      console.log(formdata)
      axios({
        method: 'post',
        url: `${API_URL}/community/movie/${this.$route.params.id}/review/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
        data: formdata,
      })
        .then((res) => {
          console.log(res.data)
          this.getMovieReviews()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setScore(score){
      this.reviewScore = score
    },
    toggleWant(){
      console.log('toggle')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/wanted/${this.$route.params.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res.data)
        this.isWanted = !this.isWanted
      })
      .catch((err) => {
        console.log(err)
      })
    },
    toggleWatch(){
      console.log('toggle')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/watched/${this.$route.params.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res.data)
        this.isWatched = !this.isWatched
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