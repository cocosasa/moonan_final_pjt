<template>
  <div class="small-card">
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
  },

}
</script>

<style>
.small-card{
  border-radius: 10px;
  overflow: hidden;
}
.small-card-img{
  width: 290px;
  height: 300px;
}
</style>