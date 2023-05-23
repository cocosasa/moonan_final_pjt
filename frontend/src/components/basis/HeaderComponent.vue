<template>
  <div class="header border shadow d-flex justify-content-between align-items-center">
    <div>
      <router-link :to="{ name: 'main' }">
        <img class="logo" src="@/assets/logo2.png" alt="">
      </router-link>
    </div>

    <div class="d-flex gap-5">
      <router-link :to="{ name: 'movies' }"><h5><strong>영화</strong></h5></router-link>
      <router-link :to="{ name: 'challenge' }"><h5><strong>추리</strong></h5></router-link>
      <router-link :to="{ name: 'recommend' }"><h5><strong>추천</strong></h5></router-link>
      <router-link :to="{ name: 'community' }"><h5><strong>커뮤</strong></h5></router-link>
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