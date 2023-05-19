import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    movieList : [
    ],
    token : null,
    recommendLists : []
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MOVIES(state, movieList){
      state.movieList = movieList
    },
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({ name:'MovieView' })
    },
    DELETE_TOKEN(state){
      state.token = null
      router.push({name : 'LogInView'})
    },
  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload){
      const { username, password1, password2 } = payload

      axios({
        method : 'post', 
        url:`${API_URL}/accounts/signup/`,
        data:{
          username, password1, password2
        }
      })
      .then(res=>{
        console.log(res.data)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err=>{
        console.log(err)
        // context.commit('SET_AUTH_ERROR', err.response)
      })
    },
    logIn(context, payload){
      const {username, password} = payload

      axios({
        method : 'post',
        url : `${API_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then(res=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    logOut(context){
      axios({
        method : 'post',
        url : `${API_URL}/accounts/logout/`,
        headers :{
          Authorization : `Token ${context.state.token}`
        }
      })
      .then(res=>{
        console.log('logout',res)
        context.commit('DELETE_TOKEN')
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  modules: {
  }
})
