<template>
  <div class="small-card" @click="goToDetail(movie.id)">
      <img class="small-card-img" :src="'https://image.tmdb.org/t/p/w500'+movie?.poster_path" alt="...">
  </div>
</template>

<script>
export default {
  name: 'MovieSmallCard',
  props: {
    movie: Object
  },
  computed: {
  },
  components: {
  },
  data() {
    return {
    }
  },
  methods: {
    goToDetail(movieId) {
      this.$router.push({ name: 'detail', params: { id: movieId } })
    },
  },

}
</script>

<style>
.small-card{
  border-radius: 5px;
  overflow: hidden;
}
.small-card-img{
  width: 220px;
}
</style>