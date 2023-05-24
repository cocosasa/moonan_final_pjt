<template>
  <div>
    <div class="d-flex">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="movie-detail-img">
      <div class="ms-5">
        <div>
          <span>{{ releasedDate }} </span>
          <h1 class="">{{ movie?.title }}</h1>
        </div>
        <div>
          <span>
            <i v-if="movie?.vote_avg >= 2" class="fa-solid fa-star" style="color: #ff0000;"></i>
            <i v-if="movie?.vote_avg >= 4" class="fa-solid fa-star" style="color: #ff0000;"></i>
            <i v-if="movie?.vote_avg >= 6" class="fa-solid fa-star" style="color: #ff0000;"></i>
            <i v-if="movie?.vote_avg >= 8" class="fa-solid fa-star" style="color: #ff0000;"></i>
            <i v-if="movie?.vote_avg >= 10" class="fa-solid fa-star" style="color: #ff0000;"></i>
            <i v-if="movie?.vote_avg < 2" class="fa-regular fa-star" style="color: #ff0000;"></i> 
            <i v-if="movie?.vote_avg < 4" class="fa-regular fa-star" style="color: #ff0000;"></i> 
            <i v-if="movie?.vote_avg < 6" class="fa-regular fa-star" style="color: #ff0000;"></i> 
            <i v-if="movie?.vote_avg < 8" class="fa-regular fa-star" style="color: #ff0000;"></i> 
            <i v-if="movie?.vote_avg < 10" class="fa-regular fa-star" style="color: #ff0000;"></i> 
            {{ movie?.vote_avg }}</span>
          <div class="d-flex">
            <div v-for="genre in movie?.genres" :key="genre.id" class="rounded-5 py-1 px-2 border me-1">
              <span>{{ genre.name }}</span>
            </div>
          </div>
        </div>
        <div class="d-flex w-25 justify-content-around">
          <div @click="toggleWant">
            <i :class="{'fa-bookmark':isWanted, 'fa-plus':!isWanted}" class="fa-solid fa-2xl"></i>
            <!-- <button  class="btn btn-secondary">보고 싶어요 </button>
            <button v-if="isWanted" class="btn btn-primary"> 보고 싶어요 </button> -->
          </div>
          <div class="flex-shrink-1"></div>
          <!-- <div class="flex-grow-1"></div> -->
          <div @click="toggleWatch">
            <i v-if="!isWatched" class="fa-solid fa-eye fa-2xl"></i>
            <i v-if="isWatched" class="fa-solid fa-eye fa-2xl" style="color: #ff0000;"></i>
            <!-- <i class="fa-solid fa-eye fa-2xl"></i> -->
            <!-- <button  class="btn btn-secondary"> 봤어요 </button>
              <button  class="btn btn-primary"> 봤어요 </button> -->
          </div>
        </div>
        <div class="mt-5">
          <p>줄거리</p>
          <p>{{ movie?.overview }}</p>
      </div>
      </div>
    </div>
    <MovieVideo v-if="movie" :movie="movie"/>
    
    <div>
      <h3>출연 배우</h3>
      <div class="d-flex row">
        <ActorItem v-for="actor in actorFor20" :key="actor.id" :actor="actor"/>

      </div>
    </div>
    <div>
      <div v-if="!isWritten">
        <h3>한 줄평 쓰기</h3>
        <div>
          <form name="reviewform" id="reviewform">
            <input type="text" v-model="reviewContent">
            <StarScore @set-score="setScore"/>
            {{ reviewScore }} 점
            
            <button @click.prevent="addReview"> 등록하기 </button>
          </form>
        </div>
      </div>
      <div v-else>
        <h3>내 한줄평</h3>
        <div v-if="!isUpdating">
          {{ myReview.content }}
          {{ myReview.score }}점
          <button @click="e=>this.isUpdating = !this.isUpdating" class="btn btn-warning">수정하기</button>
        </div>
        <div v-else>
          <form action="">
            <input type="text" v-model="reviewContent" >
            <StarScore @set-score="setScore"/>
          </form>
          <button class="btn btn-warning">수정하기</button>
        </div>
      </div>
      <div class="my-5">
        <h3>한 줄평</h3>
        <div v-if="reviews.length">
          <ReviewItem v-for="(review,idx) in reviews" :key="idx" :review="review"/>
        </div>
        <div v-else>
          작성된 한 줄평이 없습니다..
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ActorItem from '@/components/movies/ActorItem.vue';
import MovieVideo from '@/components/movies/MovieVideo.vue';
import ReviewItem from '@/components/community/ReviewItem.vue';
import StarScore from '@/components/community/StarScore.vue';
import axios from 'axios';
import { mapGetters } from 'vuex';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    ActorItem,
    MovieVideo,
    StarScore,
    ReviewItem,
  },
  created(){
    this.getMovieDetail()
    // this.getMovieReviews()
    this.getProfile()
  },
  data() {
    return {
      movie : null,
      myReview : null,
      isUpdating : false,
      isWanted : false,
      isWatched : false,
      reviewContent : null,
      reviewScore : '5.0',
    }
  },
  computed: {
    ...mapGetters(['myUserName']),
    shorten() {
      let overview = this.movie.overview

      if (overview.length > 40) {
        return overview.substring(0, 40) + '...'
      } else {
        return overview
      }
    },
    reviews(){
      return this.movie?.movie_reviews
    },
    isWritten(){
      let flag = false
      this.movie.movie_reviews.forEach( (el,index)=>{
        if (el.user == this.myUserName){
          console.log(el.user, this.myUserName)

          this.myReview = el
          this.reviewContent = el.content
          this.reviewScore = el.score
          this.movie.movie_reviews.splice( index,1 )
          flag = true
        }
      }) 
      return flag
    },
    releasedDate(){
      let datedata = new Date(this.movie?.released_date)
      console.log(datedata)
      return datedata.toLocaleDateString()
    },
    actorFor20(){
      return this.movie?.actors.slice(0,12)
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
        this.profile = res.data
        res.data.want_to_see_movies.forEach(el=>{
          if(el.id == this.$route.params.id)
            this.isWanted = true
        })
        res.data.watched_movies.forEach(el=>{
          if(el.id == this.$route.params.id)
            this.isWatched = true
        })
      })
      .catch(err => {
        console.log(err)
      })
    },
    // getMovieActors(){
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/${this.$route.params.id}/`,
    //     // headers: {
    //     //   Authorization: `Token ${this.$store.state.token}`
    //     // }
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //     this.movie = res.data
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
    getMovieReviews(){
      axios({
        method: 'get',
        url: `${API_URL}/community/reviews/`,
      })
      .then((res) => {
        console.log(res.data)
        this.movie.movie_reviews = res.data
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
          this.reviewContent = null
          this.reviewScore = null
          // this.getMovieReviews()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateReview(){
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
          this.reviewContent = null
          this.reviewScore = null
          // this.getMovieReviews()
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
  watch:{
    isWanted(){
      console.log('toggle wanted')
    },
    isWatched(){
      console.log('toggle watched')
    },
  }

}
</script>

<style>
.movie-detail-img {
  width: 400px;
}

</style>