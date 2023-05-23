<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex flex-column">
        <div class="profile-img-circle border-1 border shadow mt-3">
          <img v-if="!userData?.profile_image" class="profile-img" src="@/assets/Profile.png">
        </div>
        
        <input type="file" id="profile-image">
        <button class="btn btn-outline-dark mt-3"  @click="profileUpdate">프로필 변경</button>

      </div>
      <div class="my-5">
        <p>아이디 {{ userData?.user }}</p>
        <p>닉네임 {{ userData?.nickname }}</p>
        <p>포인트 {{ userData?.points }}</p>
      </div>
      <div v-if="!myUserName === userData?.user" class="my-auto">
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
    <div class="d-flex justify-content-between gap-3">
      <div class="w-50 p-4 profile-movielist-box">
        <h3>WANT TO WATCH</h3>
        <div class="mt-4">
          <MovieList :movie-list="wantMovieList"/>
        </div>
      </div>  
      <div class="w-50 p-4 profile-movielist-box">
        <h3>HAVE WATCHED</h3>
        <div class="mt-4">
          <MovieList :movie-list="watchedMovieList"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieList.vue'
import { mapGetters } from 'vuex'
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
    ...mapGetters(['myUserName', 'myToken']),
    watchedMovieList(){
      return this.userData?.watched_movies
    },
    wantMovieList(){
      return this.userData?.want_to_see_movies
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
          Authorization: `Token ${this.myToken}`
        }
      })
        .then(res => {
          console.dir(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    profileUpdate(){
      const formdata = new FormData()
      const image = document.querySelector('#profile-image').file
      console.log(image)
      formdata.append('profile_image', image)
      formdata.append('username', this.myUserName)
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/`,
        headers: {
          Authorization: `Token ${this.myToken}`
        },
        data: formdata
      })
        .then(res => {
          console.log(res.data)
        })
        .catch(err => { console.log(err) })
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
.profile-movielist-box{
  min-height: 456px;
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  color: white;
}
</style>