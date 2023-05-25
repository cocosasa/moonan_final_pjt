<template>
  <div class = "mt-4">
    <VueSlickCarousel :arrows="true" :dots="true" :pauseOnHover="true" :pauseOnDotsHover="true" :autoplay="true" :autoplaySpeed="5000" :variableWidth="false" :dots-color="white">
      <a href="http://localhost:8080/movies/502356" class="main-img1"><span style = "font-weight: bold; font-color: lightgrey;"><br>슈퍼 마리오 브라더스 &nbsp;&nbsp;<br> ★ 7.7&nbsp;&nbsp;&nbsp;</span></a>

      <a href="http://localhost:8080/movies/447365" class="main-img2"><span style = "font-weight: bold; font-color: lightgrey;"><br>가디언즈 오브 갤럭시 Vol.3 &nbsp;&nbsp;<br> ★ 8.1&nbsp;&nbsp;&nbsp;</span></a>

      <a href="http://localhost:8080/movies/603692" class="main-img3"><span style = "font-weight: bold; font-color: lightgrey;"><br>존 윅 4 &nbsp;&nbsp;<br> ★ 7.9&nbsp;&nbsp;&nbsp;</span></a>

      <a href="http://localhost:8080/movies/385687" class="main-img4"><span style = "font-weight: bold; font-color: lightgrey;"><br>분노의 질주: 라이드 오어 다이 &nbsp;&nbsp;<br> ★ 6.9&nbsp;&nbsp;&nbsp;</span></a>

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
    },
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
  font-size: 30px;
  color: lightgrey;
  text-align: right;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_1.jpg') no-repeat center;
  background-size: cover;
  text-decoration: none;
  -webkit-user-drag: none;
  -khtml-user-drag: none;
  -moz-user-drag: none;
  -o-user-drag: none;
}

.main-img2 {
  width: 120px;
  height: 533px;
  font-size: 30px;
  color: lightgrey;
  text-align: right;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_2.jpg') no-repeat center;
  background-size: cover;
  text-decoration: none;
  -webkit-user-drag: none;
  -khtml-user-drag: none;
  -moz-user-drag: none;
  -o-user-drag: none;
}

.main-img3 {
  width: 120px;
  height: 533px;
  font-size: 30px;
  color: lightgrey;
  text-align: right;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_3.png') no-repeat center;
  background-size: cover;
  text-decoration: none;
  -webkit-user-drag: none;
  -khtml-user-drag: none;
  -moz-user-drag: none;
  -o-user-drag: none;
}

.main-img4 {
  width: 120px;
  height: 533px;
  font-size: 30px;
  color: lightgrey;
  text-align: right;
  /* padding: 93px 45px 94px 65px; */
  box-shadow: inset -0px -100px 500px 100px #000000;
  background: url('@/assets/poster_4.jpg') no-repeat center;
  background-size: cover;
  text-decoration: none;
  -webkit-user-drag: none;
  -khtml-user-drag: none;
  -moz-user-drag: none;
  -o-user-drag: none;
}
</style>