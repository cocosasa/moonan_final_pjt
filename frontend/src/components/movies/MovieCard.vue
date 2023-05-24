<template>
  <div class="card col-3 large-card border-0 p-1" @mouseover="showTitle">
    <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" class="large-card-img h-100">
    <div class="large-card-back"></div>
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
  clear: both;
  -webkit-user-drag: none;
  padding: 0;
}
.large-card{
  background-color: rgba(255, 255, 255, 0);
  padding: 0;
}
/* .large-card-title{
  position: relative;
  bottom: 90px;
  height: 90px;
  background-color: rgba(0, 0, 0, 0.562);
  color: whitesmoke;
  text-align: center;
  margin-bottom: -80px;
  clear: both;
} */ 
.large-card :hover{
  z-index: 2;
  transform: scale(1.04) ;
  transition: all 0.3s ease-out;
}
.large-card :not(:hover){
  transition: all 0.3s ease-out ;
  z-index: 1;
}

.large-card .large-card-title {
  width: 80%;
  opacity: 0;
  transform: translateX(-50%) translateY(-50%);
  position: absolute;
  top: 80%;
  left: 50%;
  transition: all 600ms ease;
  color: white;
  text-align: center;
}
.large-card:hover .large-card-title {
  opacity: 1;
  top: 50%;
  z-index: 2;
}
.large-card .large-card-back {
  content: '';
  opacity: 0.3;
  background-color: rgba(80, 80, 80, 0.176);
  top: 50%;
  z-index: 3;
}
.large-card .large-card-title {
  font-size: 1.2rem;
  font-weight: 700;
}
.large-card .large-card-title {
  font-size: 0.9rem;
  font-weight: 300;
}
.large-card .large-card-title hr {
  border-top: 1px solid #f1f1f1;
  width: 100%;
}

</style>