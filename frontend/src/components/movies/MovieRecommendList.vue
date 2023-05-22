<template>
  <div >
    <div class="recommend-list-title">
      <h3 >자면서 보기 좋은 영화</h3>
    </div>
    <div class="d-flex justify-content-between recommend-list">
      <MovieSmallCard v-for="movie in recommendList" :key="movie.id" :movie="movie" @click="goToDetail(movie)"/>
    </div>
  </div>
</template>

<script>
import MovieSmallCard from './MovieSmallCard.vue';

export default {
  name: 'MovieRecommendList',
  components: {
    MovieSmallCard,
  },
  props : {
    recommendList : Array,
  },
  data() {
    return {

    }
  },
  computed: {
    
  },
  methods: {
    goToDetail(movieId) {
      this.$router.push({ name: 'detail', params: { id: movieId } })
    },
  },

}
</script>

<style>
.recommend-list {
  width: 100%;
  height: 300px;
  margin-top : 0px;
  margin-bottom : 50px;
  border-radius: 10px;

  background-color: rgba(255, 255, 255, 0.01);
  overflow: hidden;
}
.recommend-list-title{
  margin-top: 30px;
}
.recommend-list:first-child{
  box-shadow: inset 50px 0 27px -38px #000;
}
.recommend-list:last-child{
  box-shadow:  inset -50px 0 27px -38px #000;
}
.z-index--1{
  z-index: -1;
}
.z-index-2{
  z-index: 2;
}

</style>