<template>
  <div >
    <div class="recommend-list-title">
      <h3 >자면서 보기 좋은 영화</h3>
    </div>
    <div class="d-flex recommend-list justify-content-between">
      <MovieSmallCard class="z-index--1" v-for="movie in recommendList" :key="movie.id" :movie="movie"/>
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
  box-shadow: inset -50px 0 27px -38px #000, inset 50px 0 27px -38px #000;
  background-color: rgba(255, 255, 255, 0.01);
  overflow: hidden;
}
.recommend-list-title{
  margin-top: 30px;
}
.z-index--1{
  z-index: -1;
}

</style>