<template>
  <div>
    <VueSlickCarousel :arrows="true" :dots="true" :pauseOnHover="true" :pauseOnDotsHover="true" :autoplay="true" :autoplaySpeed="5000" :variableWidth="false">
      <div class="main-img">1</div>
      <div class="main-img">2</div>
      <div class="main-img">3</div>
      <div class="main-img">4</div>
    </VueSlickCarousel>

    <MovieRecommendList v-for="(recommendList, idx) in recommendLists" :key="idx" :recommendList="recommendList"/>

  </div>
</template>

<script>
import MovieRecommendList from '@/components/movies/MovieRecommendList'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'


export default {
  name : 'MainView',
  components : {
    MovieRecommendList,
    VueSlickCarousel,
  },
  created() {
    this.getMovies()
  },
  data () {
    return {
      settings: {
        arrows: true,
        dots: true,
      },
    }
  },
  computed :{
    movieList (){
      return this.$store.state.movieList
    },
    recommendLists() {
      return [
        this.$store.state.popularMovieList.slice(10,16),
        this.$store.state.popularMovieList.slice(20,26),
        this.$store.state.popularMovieList.slice(120,126),
    ]
    }
  },
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getGenres')
    }
  },

}
</script>

<style>
.main-img {
  width: 120px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset 96px 50px 250px 29px #000, inset -54px -50px 250px 20px #000;
  background: url('@/assets/img.bmp') no-repeat center;
  background-size: cover;
}
</style>