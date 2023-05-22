<template>
  <div class="review-container">
    <p>{{ review.user }}</p>
    <p>{{ review.content }}</p>
    <p>{{ review.score }}</p>
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