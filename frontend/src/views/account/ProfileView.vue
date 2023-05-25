<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex flex-column">
        <div class="profile-img-circle border-1 border shadow mt-3" @click="changeFile">
          <p id = "change-img">사진 변경</p>
          <img v-if="!userData?.profile_image" class="profile-img" src="@/assets/Profile.png">
          <img v-if="userData?.profile_image" class="profile-img" :src="`${BASE_URL}${userData?.profile_image}`">
        </div>
        <div v-if="isMyProfile">
          <input type="file" id="profile-image" @change="inputImage" ref="profile_image" class="btn">
          <button class="btn btn-outline-light mt-3"  @click="profileUpdate">프로필 변경</button>
        </div>
      </div>
      <div class="my-auto">
        <p>아이디&nbsp;&nbsp;&nbsp;&nbsp;{{ userData?.user.username }}</p>
        <!-- <p>닉네임 {{ userData?.nickname }}</p> -->
        <p>포인트&nbsp;&nbsp;&nbsp;&nbsp;{{ userData?.points }}</p>
      </div>
      <div v-if="!isMyProfile" class="my-auto">
        <button @click="toggleFollow" v-if="!isFollowing">팔로우</button>
        <button @click="toggleFollow" v-if="isFollowing">언팔로우</button>
      </div>
      <div class="d-flex my-auto">
        <!-- <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>2</p>
          <p>Reviews</p>
        </div> -->
        <div class="profile-info">
          <p>{{userData?.user.followings_count}}</p>
          <p>Followings</p>
        </div>
        <div class="profile-info">
          <p>{{userData?.user.followers_count}}</p>
          <p>Follower</p>
        </div>
      </div>
    </div>
    <hr>
    <div class="d-flex justify-content-between gap-3">
      <div class="w-50 p-4 profile-movielist-box">
        <h3>WANT TO WATCH</h3>
        <span>{{ wantMovieList.length }}</span>
        <div class="mt-4">
          <MovieList :movie-list="wantMovieList"/>
        </div>
      </div>  
      <div class="w-50 p-4 profile-movielist-box">
        <h3>HAVE WATCHED</h3>
        <span>{{ watchedMovieList.length }}</span>
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
      comments:null,
      file:null,
    }
  },
  computed: {
    ...mapGetters(['myUserName', 'myToken']),
    watchedMovieList(){
      return this.userData?.watched_movies ? this.userData?.watched_movies : []
    },
    wantMovieList(){
      return this.userData?.want_to_see_movies ? this.userData?.want_to_see_movies : []
    },
    BASE_URL(){
      return 'http://127.0.0.1:8000'
    },
    isMyProfile(){
      return this.myUserName == this.$route.params.username
    },
    isFollowing(){
      return this.userData?.user.followers.includes(this.$store.state.userData?.id) ? true : false
    }
  },
  methods: {
    getUserInfomation(){
      axios({
        method : 'get',
        url : `${API_URL}/accounts/profile/${this.$route.params.username}/`,
      })
      .then(res=>{
        console.dir(res.data)
        if(this.$route.params.username == this.myUserName){
          this.$store.dispatch('changeUserData', res.data)
        }
        this.userData = res.data
      })
      // .then(()=>{
      //   axios({
      //     method: 'get',
      //     url: `${API_URL}/community/${this.$route.params.username}/`,
      //   })
      //   .then(res => {
      //     console.dir(res.data)
      //     this.comments = res.data
      //   })
      //   .catch((e)=>{
      //     console.log(e)
      //   })
      // })
      .catch(err=>{
        console.log(err)
        alert('존재하지 않는 사용자입니다.')
        this.$router.back()
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
          this.getUserInfomation()
        })
        .catch(err => {
          console.log(err)
        })
    },
    inputImage() {
      this.file = this.$refs.profile_image.files[0]
      console.log(this.file)
    },
    changeFile() {
      document.querySelector('#profile-image').click()
    },
    profileUpdate(){
      if(!this.file){
        return
      }
      const formdata = new FormData()
      // formdata.append('points', this.userData.points)
      formdata.append('profile_image', this.file)
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.myToken}`,
          'Content-Type': 'multipart/form-data'
        },
        data: formdata
      })
        .then(res => {
          console.log(res.data)
          this.getUserInfomation()
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
  border-radius: 50%;
}
.profile-img-circle:hover {
  opacity: 0.5;
  content : '이미지 수정';
}
.profile-img-circle:hover #change-img {
  opacity: 1.0;
  content : '이미지 수정';
}
.profile-img{
  position: relative;
  -webkit-user-drag: none;
  width: 110%;
  height: 110%;
  top: -5%;
  left: -5%;
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
#profile-image{
  width: 0px;
  visibility: hidden;
  margin: 0px;
}
#change-img {
  position: absolute; opacity: 0;
  margin-top: 100px;
  margin-left: 40px;
}
</style>