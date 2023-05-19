<template>
  <div class="small-card">
    {{ movie.poster_path }}
      <img class="small-card-img" :src="'https://image.tmdb.org/t/p/w500'+movie?.poster_path" alt="...">
      <img class="small-card-img" src="@/assets/img.jpg"  alt="...">
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
  },

}
</script>

<style>
.small-card{
  overflow: hidden;
}
.small-card-img{
  width: 200px;
  height: 300px;
}
</style>