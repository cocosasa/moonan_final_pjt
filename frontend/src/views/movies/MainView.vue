<template>
  <div class = "mt-4">
    <VueSlickCarousel :arrows="true" :dots="true" :pauseOnHover="true" :pauseOnDotsHover="true" :autoplay="true" :autoplaySpeed="5000" :variableWidth="false" :dots-color="white">
      <div class="main-img1"></div>
      <div class="main-img2"></div>
      <div class="main-img3"></div>
      <div class="main-img4"></div>
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
import _ from 'lodash'


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
      return _.sampleSize(this.$store.state.recommendLists, 2)
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
.main-img1 {
  width: 120px;
  height: 533px;
  font-size: 50px;
  text-align: center;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_1.jpg') no-repeat center;
  background-size: cover;
}

.main-img2 {
  width: 120px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_2.jpg') no-repeat center;
  background-size: cover;
}

.main-img3 {
  width: 120px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_3.png') no-repeat center;
  background-size: cover;
}

.main-img4 {
  width: 120px;
  height: 533px;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_4.jpg') no-repeat center;
  background-size: cover;
}
</style>