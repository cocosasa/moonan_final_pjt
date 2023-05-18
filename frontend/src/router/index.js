import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/components/movies/MainView'
import SearchView from '@/components/movies/SearchView'
import MovieView from '@/components/movies/MovieView'
import MovieDetailView from '@/components/movies/MovieDetailView'
import ProfileView from '@/components/account/ProfileView'
import SignUpView from '@/components/account/SignUpView'
import LogInView from '@/components/account/LogInView'
import LogOutView from '@/components/account/LogOutView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },

  {
    path: '/movies',
    name: 'MovieView',
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
    component: SearchView
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
