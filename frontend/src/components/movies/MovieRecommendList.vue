<template>
  <div class="mt-5">
    <div class="mb-3">
      <span class="recommend-list-title">{{ recommendList.creteria }}</span>
    </div>
    <VueSlickCarousel class = "ms-2" v-bind="settings" >
        <MovieSmallCard v-for="movie in recommendList.movielist" :key="movie.id" :movie="movie" @click="goToDetail(movie)"/>
    </VueSlickCarousel>
    
  </div>
</template>

<script>
import MovieSmallCard from './MovieSmallCard.vue';
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'MovieRecommendList',
  components: {
    MovieSmallCard,
    VueSlickCarousel,
  },
  props : {
    recommendList : Object,
  },
  data() {
    return {
      settings: {
        "arrows": true,
        "dots": true,
        "infinite": true,
        "slidesToShow": 5,
        "slidesToScroll": 2,
        // "autoplay": true,
        "speed": 300,
        "autoplaySpeed": 2000,
        "cssEase": "linear"
      }
    }
  },
  computed: {
    
  },
  methods: {
    goToDetail(movieId) {
      this.$router.push({ name: 'detail', params: { id: movieId } })
    },
    stopClick(e){
      console.log('dd', e)
    }
  },

}
</script>

<style>
.recommend-list {
  width: 100%;
  height: 350px;
  margin-top : 0px;
  margin-bottom : 50px;
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.01);
  overflow: hidden;
}
.recommend-list-title {
  --padding: 1.5rem;
  font-size: 2em;
  position: relative;
  cursor: pointer;
}

.recommend-list-title::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -1rem;
  height: 4px;
  width: calc(100%);
  background: red;
}

@media (hover) {
  .recommend-list-title:hover::after {
    transform: scaleX(1);
    margin-left: 0;
  }

  .recommend-list-title::after {
    transform: scaleX(0);
    margin-left: 50%;
    transform-origin: left;
    transition: transform 500ms ease, margin-left .5s ease;
  }
}
.z-index--1{
  z-index: -1;
}
.z-index-2{
  z-index: 2;
}

.slick-next:before{
  color: white;
}
.slick-prev:before{
  color: white;
}

</style>