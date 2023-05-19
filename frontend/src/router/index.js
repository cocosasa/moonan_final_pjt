import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/movies/MainView'
import SearchResultView from '@/views/movies/SearchResultView'
import ChallengeView from '@/views/community/ChallengeView'
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import ProfileView from '@/views/account/ProfileView'
import SignUpView from '@/views/account/SignUpView'
import LogInView from '@/views/account/LogInView'
import LogOutView from '@/views/account/LogOutView'
import CommunityView from '@/views/community/CommunityView'
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
    path: '/movies/:id',
    name: 'detail',
    component: MovieDetailView
  },

  {
    path: '/profile/:id',
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
