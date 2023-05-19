<template>
  <div class="card col-3 large-card border-0">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="large-card-img h-100">
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
</style>