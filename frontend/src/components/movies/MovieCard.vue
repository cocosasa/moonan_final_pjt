<template>
  <div class="card">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
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
  },

}
</script>

<style>

</style>