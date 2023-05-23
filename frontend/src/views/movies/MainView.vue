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
      return this.$store.state.recommendLists
    }
  },
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getGenres')
      this.$store.dispatch('getRecommends')
    }
  },

}
</script>

<style>
.carousel{
  width: 160%;
  left: -30%;
  top: 0px;
} 
.main-img {
  width: 120px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/img.bmp') no-repeat center;
  background-size: cover;
}
</style>