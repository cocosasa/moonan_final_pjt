import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/movies/MainView'
import SearchResultView from '@/views/movies/SearchResultView'
import ChallengeView from '@/views/community/ChallengeView'
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import MovieRecommendView from '@/views/movies/MovieRecommendView'
import ProfileView from '@/views/account/ProfileView'
import LogInView from '@/views/account/LogInView'
import CommunityView from '@/views/community/CommunityView'
import QuestionFormView from '@/views/community/QuestionFormView'
import QuestionDetailView from '@/views/community/QuestionDetailView'
import NotFound404 from '@/views/account/NotFound404'
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
    path: '/login',
    name: 'LogInView',
    component: LogInView
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
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect:'/404',
    component: NotFound404
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
