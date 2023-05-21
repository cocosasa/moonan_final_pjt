<template>
  <div class="card col-3 large-card border-0 p-1" @mouseover="showTitle">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="large-card-img h-100">
      <div class="large-card-title">
        <div>{{ movie.title }}</div>
        <div>{{ movie.released_date }}</div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object
  },
  computed: {
    shorten() {
      let overview = this.movie.overview

      if (overview.length > 40) {
        return overview.substring(0, 40) + '...'
      } else {
        return overview
      }
    }
  },
  components: {
  },
  data() {
    return {
    }
  },
  methods: {
    showTitle(){

    }
  },

}
</script>

<style>
.large-card-img{
  padding: 0;
}
.large-card{
  padding: 0;
}
.large-card-title{
  position: relative;
  bottom: 90px;
  height: 90px;
  background-color: rgba(0, 0, 0, 0.562);
  color: whitesmoke;
  text-align: center;
  margin-bottom: -80px;
}

</style>