<template>
  <div>
    <div class="quiz_img" v-if="movie"> 
        <div class="quiz_hint" :style="`top: ${(img_size_y - 100) * 0.5}px; left: ${(img_size_x - 100) * 0.5}px; background-position : ${offset_x}% ${offset_y}%;background-image: url('${imageURL}');`"></div>
        <div class="quiz_hint" :style="`top:${img_size_y - 100}px; left: ${img_size_x - 100}px; background-position : 100% 100%;background-image: url('${imageURL}');`"></div>
        <div class="quiz_hint" :style="`top: 0%;left: 0%; background-position : 0% 0%; background-image: url('${imageURL}');`"></div>
        <div class="quiz_hint" :style="`top: 0%;left:${(img_size_x - 100) * 0.5}px; background-position : 50% 0%; background-image: url('${imageURL}');`"></div>
      </div>
      <img src="@/assets/img.jpg">
  </div>
</template>

<script>
export default {
  name:'QuizItem',
  data() {
    return {
      img_size_x: 500,
      img_size_y: 750,
      hint_size_x: 125,
      hint_size_y: 750,
      offset_x: 50,
      offset_y: 50,
    }
  },
  props:{
    movie : Object
  },
  computed :{
    imageURL(){
      console.log(this.movie)
      return 'https://image.tmdb.org/t/p/w500/'+this.movie.poster_path
    }
  }
}
</script>

<style>
.quiz_img{
  margin: 0 auto;
  width: 264px;
  height: 366px;
  position: relative;
}
.quiz_hint{
  position: absolute;
  width: 200px;
  height: 170px;
}
</style>