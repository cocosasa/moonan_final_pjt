<template>
  <div class="header border shadow d-flex justify-content-between align-items-center">
    <div>
      <router-link :to="{ name: 'main' }">
        <img class="logo" src="@/assets/logo2.png" alt="">
      </router-link>
    </div>

    <div>
      <router-link :to="{ name: 'movies' }">영화</router-link> | 
      <router-link :to="{ name: 'challenge' }">추리</router-link> | 
      <router-link :to="{ name: 'recommend' }">추천</router-link> | 
      <router-link :to="{ name: 'community' }">커뮤니티</router-link> | 
    </div>

    <div>
      <SearchBar/>
    </div>

    <router-link v-if="isLogin" :to="{ name: 'LogOutView' }">LogOut</router-link>
    <div v-if="isLogin">
      <router-link :to="{ name: 'profile', params:{ username,} }">
        <div class="profile-circle">
          <img class="profile-icon" src="@/assets/Profile.png" alt="">
        </div>
      </router-link>
    </div>

    <div v-if="!isLogin"> | 
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link>
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
    username (){ 
      return this.$store.state.username
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
    padding: 50px 30px;
  }
  .profile-circle{
    width: 50px;
    border: 2px solid black;
    border-radius: 25px;
    overflow: hidden;
  }
  .profile-icon{
    width: 100%;
  }
</style>