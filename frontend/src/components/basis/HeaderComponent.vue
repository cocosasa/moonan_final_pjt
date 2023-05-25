<template>
  <div class="header shadow d-flex justify-content-between align-items-center">
    <div id="to-nav">
      <router-link :to="{ name: 'main' }">
        <img class="logo" src="@/assets/logo2.png" alt="">
      </router-link>
    </div>

    <div class="d-flex gap-4">
      <router-link :to="{ name: 'movies' }"><h5><strong>Movie</strong></h5></router-link>
      <router-link :to="{ name: 'challenge' }"><h5><strong>Clue</strong></h5></router-link>
      <router-link :to="{ name: 'recommend' }"><h5><strong>Recommend</strong></h5></router-link>
      <router-link :to="{ name: 'community' }"><h5><strong>Community</strong></h5></router-link>
    </div>

    <div>
      <SearchBar/>
    </div>

    <router-link v-if="isLogin" :to="{ name: 'LogOutView' }">로그아웃</router-link>
    <div v-if="isLogin">
      <router-link :to="{ name: 'profile', params:{ username: myUserName } }">
        <div class="profile-circle">
          <img v-show="!myUserData?.profile_image" class="profile-icon" src="@/assets/Profile.png" alt="">
          <img v-show="myUserData?.profile_image" class="profile-icon" :src="`http://127.0.0.1:8000${myUserData?.profile_image}`" alt="">
        </div>
      </router-link>
    </div>

    <div v-if="!isLogin"> | 
      <router-link :to="{ name: 'LogInView' }">로그인</router-link> | 
      <!-- <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> -->
    </div>
  </div>
</template>

<script>
import SearchBar from './SearchBar.vue';

export default {
  name: 'HeaderComponent',
  components: {
    SearchBar,
  },
  data() {
    return {

    }
  },
  computed: {
    isLogin(){
      return this.$store.state.token ? true : false
    },
    myUserName(){ 
      return this.$store.getters.myUserName
    },
    myUserData(){
      return this.$store.getters.myUserData
    }

  },
  methods: {

  },

}
</script>

<style>
  .logo{
  width: 280px;
  }
  .header{
    height: 100px;
    background-color: #282828;
    padding: 50px 30px;
    border: none;
  }
  .profile-circle{
    width: 50px;
    height: 50px;
    border: 1px solid snow;
    border-radius: 50%;
    overflow: hidden;
  }
  .profile-icon{
    position: relative;
    -webkit-user-drag: none;
    width: 110%;
    height: 110%;
    top: -5%;
    left: -5%;
  }
</style>