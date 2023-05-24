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
    popularMovieList : [
    ],
    voteAvgMovieList : [
    ],
    recommendLists : [
    ],
    questionList :[
    ],
    genreList : [
    ],
    token : null,
    username : null,
    points : null
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
    myUserName(state){
      return state.username
    },
    // myNickName(state){
    //   return state.nickname
    // },
    myToken(state){
      return state.token
    },
    myPoints(state){
      return state.points
    }
  },
  mutations: {
    GET_POPULARMOVIES(state, movieList){
      state.popularMovieList = movieList
    },
    GET_VOTEAVGMOVIES(state, movieList){
      state.voteAvgMovieList = movieList
    },
    GET_GENRES(state, genres){
      state.genreList = genres
    },
    GET_RECOMMENDS(state, recommends){
      state.recommendLists = recommends
    },
    GET_QUESTIONS(state, list){
      state.questionList = list
    },
    SAVE_TOKEN(state, data){
      const {token, username, points} = data
      state.token = token
      state.username = username
      state.points = points
      router.push({ name:'movies' })
    },
    DELETE_TOKEN(state){
      state.token = null
      state.username = null
      state.points = null
      router.push({name : 'LogInView'})
    },
    ADD_MY_POINTS(state, points){
      state.points += points
    }
  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_POPULARMOVIES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/vote_avg/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_VOTEAVGMOVIES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    getGenres(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genres/`,
      })
      .then(res=>{
        context.commit('GET_GENRES', res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getRecommends(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/recommend/`,
      })
      .then(res=>{
        console.log(res.data)
        context.commit('GET_RECOMMENDS', res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getQuestions(context){
      axios({
        method: 'get',
        url: `${API_URL}/community/questions/`,
        // headers : {
        //   Authorization : `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_QUESTIONS', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload){
      const { username, password1, password2 } = payload
      var token = ''
      axios({
        method : 'post', 
        url:`${API_URL}/accounts/signup/`,
        data:{
          username, password1, password2
        }
      })
      .then(res=>{
        console.log(res.data)
        token = res.data.key

      })
      .then(()=>{
        axios({
          method : 'post', 
          url:`${API_URL}/accounts/profile/`,
          headers : {
            Authorization : `Token ${token}`
          },
        })
        .then(res=>{
          console.log(res.data)
          context.commit('SAVE_TOKEN', {
            token, username, points:res.data.points
          })
        })
        .catch(err=>{console.log(err)})
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
        console.log(res.data)
        context.commit('SAVE_TOKEN', {
            token:res.data.key,
            username,
        })
        // axios({
        //   method : 'get',
        //   url : `${API_URL}/accounts/profile/${username}/`,
        // })
        // .then(response=>{
        //   console.dir(response.data)
          
        // })
        // .catch(err=>{
        //   console.log(err)
        // })
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
    },
    setMyPoints(context, points){
      context.dispatch('SET_MY_POINTS', points)
    }
  },
  modules: {
  }
})
