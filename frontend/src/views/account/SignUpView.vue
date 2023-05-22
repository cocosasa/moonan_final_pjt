<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp" >
    </form>
  </div>
</template>

<script>
// import AccountErrorList from '@/components/AccountErrorList'
// import { mapGetters } from 'vuex'
export default {
  name: 'SignUpView',
  components : {
    // AccountErrorList,
  },
  data() {
    return{
      username : null,
      nickname : null,
      password1: null,
      password2: null,
    }
  },
  computed :{
    // ...mapGetters(['isAuthError'])
  },
  methods: {
    signUp(){
      const username = this.username
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2
      if(!username.trim()){
        alert('아이디를 확인해주세요')
        return
      }
      else if(!nickname.trim()) {
        alert('닉네임을 확인해주세요')
        return
      }
      else if(!password1.trim() || !password2.trim() || password1 != password2) {
        alert('비밀번호를 확인해주세요')
        return
      }

      const payload = {
        username,
        nickname,
        password1,
        password2,
      }
      this.$store.dispatch('signUp', payload )
    }
  },

}
</script>
