<template>
  <div class="review-container" style = "color: black;">
    <p>{{ review.user }}</p>
    <p>{{ review.content }}</p>
    <p>{{ review.score }}점</p>
  </div>
</template>

<script>
export default {
  name:'ReviewItem',
  props:{
    review : Object,
  }
}
</script>

<style>
.review-container{
  background-color: whitesmoke;
}
</style>