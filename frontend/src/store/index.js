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
      [
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/xSDdRAjxKAGi8fUBLOqSrBhJmF0.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/gH4UTm1wY6HWiv1UBkT7IkiIxjD.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        }
      ],
      [
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        },
        {
          id:502356,
          overview:"따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
          popularity:8501.774,
          poster_path:"/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
          released_date:"2023-04-05",
          title:"슈퍼 마리오 브라더스",
          vote_avg:7.6,
        }
      ],

    ],
    questionList :[
    ],
    token : null,
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
  },
  mutations: {
    GET_POPULARMOVIES(state, movieList){
      state.popularMovieList = movieList
    },
    GET_VOTEAVGMOVIES(state, movieList){
      state.voteAvgMovieList = movieList
    },
    GET_QUESTIONS(state, list){
      state.questionList = list
    },
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({ name:'movies' })
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
        url: `${API_URL}/api/v1/`,
      })
        .then((res) => {
          console.log(res.data)
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
          console.log(res.data)
          context.commit('GET_VOTEAVGMOVIES', res.data)
        })
        .catch((err) => {
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
