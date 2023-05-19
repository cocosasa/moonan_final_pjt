<template>
  <div>
    <div class="quiz_img" > 
        <div class="quiz_hint" :style="`top: ${(img_size_y - 100) * 0.5}px;left: ${(img_size_x - 100) * 0.5}px; background-position : ${offset_x}% ${offset_y}%;`"></div>
        <div class="quiz_hint" :style="`top:${img_size_y - 100}px; left: ${img_size_x - 100}px; background-position : 100% 100%;`"></div>
        <div class="quiz_hint" :style="`top: 0%;left: 0%; background-position : 0% 0%;`"></div>
        <div class="quiz_hint" :style="`top: 0%;left:${(img_size_x - 100) * 0.5}px; background-position : 50% 0%;`"></div>
      </div>
      <img src="@/assets/img.jpg">
  </div>
</template>

<script>
export default {
  name:'QuizItem',
  data() {
    return {
      img_size_x: 264,
      img_size_y: 366,
      offset_x: 50,
      offset_y: 50,
    }
  },
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
  background-image: url('@/assets/img.jpg');
  width: 100px;
  height: 100px;
}
</style>