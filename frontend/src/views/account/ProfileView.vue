<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex flex-column">
        <div class="profile-img-circle border-1 border shadow mt-3">
          <img class="profile-img" src="@/assets/Profile.png">
        </div>
        <button class="btn btn-outline-dark mt-3" >이미지 변경</button>
      </div>
      <div class="my-5">
        <p>아이디 {{ userData?.user }}</p>
        <p>닉네임 {{ userData?.nickname }}</p>
        <p>포인트 {{ userData?.points }}</p>
      </div>
      <div v-if="!myUsername === userData.user" class="my-auto">
        <button @click="toggleFollow">팔로우</button>
      </div>
      <div class="d-flex">
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>2</p>
          <p>Reviews</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>Followings</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>Follower</p>
        </div>
      </div>
    </div>
    <hr>
    <div>
      <h3>WANT TO WATCH</h3>
      <MovieList :movie-list="wantMovieList"/>
    </div>
    <div>
      <h3>HAVE WATCHED</h3>
      <MovieList :movie-list="watchedMovieList"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components:{
    MovieList,
  },
  created(){
    this.getUserInfomation()
  },
  data() {
    return {
      userData:null,
      user:null,
    }
  },
  computed: {
    myUsername(){
      return this.$store.state.username
    },
    watchedMovieList(){
      return this.userData.watched_movies
    },
    wantMovieList(){
      return this.userData.want_to_see_movies
    },
  },
  methods: {
    getUserInfomation(){
      axios({
        method : 'get',
        url : `${API_URL}/accounts/profile/${this.$route.params.username}/`,
      })
      .then(res=>{
        console.dir(res.data)
        this.userData = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    toggleFollow(){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/follow/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res => {
          console.dir(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },

}
</script>

<style>
.profile-img-circle{
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 100px;
}
.profile-img{
  width: 100%;
  height: 100%;
}
.profile-info{
  margin-top: 80px;
  margin-bottom: 60px;
  padding-left: 60px;
  padding-right: 60px;
  border-right: 1px solid;
  align-items: center;
}
.profile-info:last-of-type{
  border-right: 0px solid;
}
.profile-info > p {
  text-align: center;
}
</style>