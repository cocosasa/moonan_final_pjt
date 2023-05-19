<template>
  <div class="header border shadow-lg d-flex justify-content-between align-items-center">
    <div>
      <router-link :to="{ name: 'main' }">
        <img class="logo" src="@/assets/logo2.png" alt="">
      </router-link>
    </div>
    <div>
      <router-link :to="{ name: 'movies' }">영화</router-link> | 
      <router-link :to="{ name: 'challenge' }">추리</router-link> | 
      <router-link :to="{ name: 'movies' }">추천</router-link> | 
      <router-link :to="{ name: 'movies' }">커뮤니티</router-link> | 
      
      <login>
        <router-link :to="{ name: 'LogOutView' }">LogOut</router-link>
      </login>
      <login> | 
        <router-link :to="{ name: 'LogInView' }">LogInPage</router-link> | 
        <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link>
      </login>
      
    </div>
    <div>
      <input type="text">
      <button>search</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderComponent',
  components: {

  },
  data() {
    return {

    }
  },
  computed: {

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
  }
</style>