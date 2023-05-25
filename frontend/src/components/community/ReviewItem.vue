<template>
  <div class="review-container rounded d-flex gap-3" style = "color: black;">
    <p style="color: azure">{{ review.user }}</p>
    <p style="color: wheat">★ {{ review.score }}</p>
    <p style="color: lightcoral">{{ review.content }}</p>
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
  background-color: rgba(0, 0, 0, 0.192);
  padding: 20px;
  margin-bottom: 10px;
}
.review-container:last-child {
  margin-bottom: 0;
}
</style>