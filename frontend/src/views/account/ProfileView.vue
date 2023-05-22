<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="profile-img-circle">
        <img class="profile-img" src="@/assets/moonanface.png">
      </div>
      <div class="mt-5">
        <p>{{ userData?.nickname }}</p>
        <p>{{ userData?.points }}</p>
      </div>
      <div v-if="mynickname != userData?.nickname">
        <button @click="toggleFollow">팔로우</button>
        <button>팔로우</button>
      </div>
      <div class="d-flex">
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
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
      <div>영화</div>
    </div>
    <div>
      <h3>WANT TO WATCH</h3>
      <div>영화</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
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
    mynickname(){
      return this.$store.state.username
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
  margin-top: 60px;
  margin-bottom: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border-right: 1px solid;
  align-items: center;
}
.profile-info > p {
  text-align: center;
}
</style>