<template>
  <div class="overflow-visible back-drop" :style="{ background: `linear-gradient(to bottom, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.2)), url(https://image.tmdb.org/t/p/w1280${this.movie?.backdrop_path}) no-repeat center` }">
    <div></div>
    <div class="d-flex mt-3 z-1">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="movie-detail-img">
      <div class="ms-5">
        <div>
          <br>
          <span>{{ releasedDate }} 개봉</span>
          <h1 class="">{{ movie?.title }}</h1>
        </div>
        <hr>
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
          <div class="d-flex mt-3">
            <div v-for="genre in movie?.genres" :key="genre.id" class="rounded-5 py-1 px-2 border me-1">
              <span>{{ genre.name }}</span>
            </div>
          </div>
        </div>
        <div class="d-flex w-25 justify-content-around mt-5">
          <div @click="toggleWant">
            <i :class="{'fa-bookmark':isWanted, 'fa-plus':!isWanted}" class="fa-solid fa-2xl" :style="{'color:#ff0000;': this.isWanted  }"></i>
          </div>
          <div class="flex-shrink-1"></div>
          <div @click="toggleWatch">
            <i v-if="!isWatched" class="fa-solid fa-eye fa-2xl"></i>
            <i v-if="isWatched" class="fa-solid fa-eye fa-2xl" style="color: #ff0000;"></i>
          </div>
        </div>
        <div class="mt-5 ps-3" v-if="movie?.overview">
          <p style = "font-size: 20px;"> Overview </p>
          <p id = "overview">{{ movie?.overview }}</p>
      </div>
      </div>
    </div>
    <hr style = "background-color: white; height: 5px;">
    <br>
    <br>
    <MovieVideo class = "mt-5 justify-content: center;" style = "border: solid 3px white overline" v-if="movie" :movie="movie"/>
    <hr style = "background-color: white; height: 5px;">
    <div>
      <br>
      <h2>출연 배우</h2>
      <br>
      <div class="d-flex row">
        <ActorItem v-for="actor in actorFor20" :key="actor.id" :actor="actor"/>
      </div>
    </div>
    <hr style = "background-color: white; height: 5px;">
    <div>
      <div v-if="!myReview">
        <h3>한 줄평 쓰기</h3>
        <div>
          <form @submit.prevent="addReview" name="reviewform" id="reviewform">
            <input type="text" class="rounded" style = "width:500px; height: 50px;" v-model="reviewContent">
            <StarScore @set-score="setScore"/>
            <span class="fs-5">{{ reviewScore }} 점</span>
            <button class="ms-3 btn btn-danger"> 등록하기 </button>
            <br>
            </form>
        </div>
      </div>
      <div v-else>
        <h3>내 한줄평</h3>
        <div v-if="!isUpdating" class="m-3">
          <span>{{ myReview?.content }}</span><br>
          <span>{{ myReview?.score }}점</span>
          <button @click="e=>this.isUpdating = !this.isUpdating" class="btn btn-warning ms-5 mt-2">수정하기</button>
          <button @click="deleteComment" class="btn btn-danger ms-3 mt-2">삭제</button>
        </div>
        <div v-else>
          <form @submit.prevent="updateReview">
            <input type="text" class="rounded" style = "width:500px; height: 50px;" v-model="reviewContent" >
            <StarScore @set-score="setScore"/>
            <span class="fs-5">{{ reviewScore }} 점</span>
            <button class="btn btn-warning ms-3">수정완료</button>
            <button @click="e => this.isUpdating = !this.isUpdating" class="btn btn-danger ms-3">취소</button>
          </form>
        </div>
      </div>
      <hr>
      <div class="my-5">
        <h3>한 줄평</h3>
        <div v-if="reviews?.length" class="review rounded">
          <ReviewItem v-for="(review,idx) in reviews" :key="idx" :review="review"/>
        </div>
        <div v-else class="review rounded p-4">
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
import { mapGetters } from 'vuex';
import axios from 'axios';

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
    ...mapGetters(['myUserName', 'isLogin']),
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
          this.isWritten()
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
    isWritten() {
      let flag = false
      this.movie?.movie_reviews.forEach((el) => {
        if (el.user == this.myUserName) {
          console.log(el.user, this.myUserName)

          this.myReview = el
          this.reviewContent = el.content
          this.reviewScore = el.score
          flag = true
        }
      })
      return flag
    },
    addReview(){
      if (!this.isLogin) {
        this.$store.dispatch('alertLogin')
        return
      }
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
          // this.reviewContent = null
          // this.reviewScore = null
          this.getMovieDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateReview(){
      // if (!this.isLogin) {
      //   this.$store.dispatch('alertLogin')
      //   return
      // }
      const content = this.reviewContent
      const score = this.reviewScore
      // if(!this.content){
      //   return
      // }
      var formdata = new FormData()
      formdata.append('content', content)
      formdata.append('score', score)

      console.log(this.myReview)
      axios({
        method: 'PUT',
        url: `${API_URL}/community/reviews/${this.myReview.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        },
        data: formdata,
      })
        .then((res) => {
          console.log(res.data)
          this.reviewContent = null
          this.reviewScore = null
          this.isUpdating = false
          this.getMovieDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment(){
      if (!this.isLogin) {
        this.$store.dispatch('alertLogin')
        return
      }
      axios({
        method: 'delete',
        url: `${API_URL}/community/reviews/${this.myReview.id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`,
        }
      })
        .then((res) => {
          console.log(res.data)
          this.reviewContent = null
          this.reviewScore = null
          this.isUpdating = false
          this.myReview = null
          this.getMovieDetail()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setScore(score){
      this.reviewScore = score
    },
    toggleWant(){
      if(!this.isLogin){
        this.$store.dispatch('alertLogin')
        return
      }
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
        if (this.isWatched && this.isWanted)
          this.isWatched = false
      })
      .catch((err) => {
        console.log(err)
      })
    },
    toggleWatch(){
      if (!this.isLogin) {
        this.$store.dispatch('alertLogin')
        return
      }
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
        if (this.isWatched && this.isWanted)
          this.isWanted = false
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

<style scoped>
.movie-detail-img {
  width: 400px;
}

#overview {
  border: solid 1px white;
  padding: 3%;
  border-radius: 8px;
}
.review{
  padding: 10px;
  min-height: 100px;
  background-color: #ffffff2f;
}
.back-drop {
  width: 1200x;
  height: 600px;
  /* left: -1000px; */
  background-size: cover;
  /* background-repeat: no-repeat;
  background-position: center; */
  /* background-attachment: fixed; */
  /* background: linear-gradient(to bottom, rgb(0, 0, 0), rgba(0, 0, 0, 0)); */
}
</style>