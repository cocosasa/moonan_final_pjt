import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/movies/MainView'
import SearchResultView from '@/views/movies/SearchResultView'
import ChallengeView from '@/views/community/ChallengeView'
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import MovieRecommendView from '@/views/movies/MovieRecommendView'
import ProfileView from '@/views/account/ProfileView'
import SignUpView from '@/views/account/SignUpView'
import LogInView from '@/views/account/LogInView'
import LogOutView from '@/views/account/LogOutView'
import CommunityView from '@/views/community/CommunityView'
import QuestionFormView from '@/views/community/QuestionFormView'
import QuestionDetailView from '@/views/community/QuestionDetailView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },

  {
    path: '/movies',
    name: 'movies',
    component: MovieView
  },

  {
    path: '/recommend',
    name: 'recommend',
    component: MovieRecommendView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/logout',
    name: 'LogOutView',
    component: LogOutView
  },

  {
    path: '/search/:keyword',
    name: 'search',
    component: SearchResultView
  },

  {
    path: '/challenge',
    name: 'challenge',
    component: ChallengeView
  },
  
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },

  {
    path: '/community/post',
    name: 'postquestion',
    component: QuestionFormView
  },

  {
    path: '/community/:id',
    name: 'questiondetail',
    component: QuestionDetailView
  },

  {
    path: '/movies/:id',
    name: 'detail',
    component: MovieDetailView
  },

  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
