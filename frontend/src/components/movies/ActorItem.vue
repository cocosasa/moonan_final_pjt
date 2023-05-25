<template>
  <div class="col-2" v-if="actor.image_path">
    <div v-if="!actor.image_path">
      <div class="actor-card-null actor-card"></div>
      <p>{{ actor.name }}</p>
    </div>
    <div  v-if="actor.image_path">
      <img :src="`https://image.tmdb.org/t/p/w500/${actor?.image_path}`" class="actor-card" >
      <p>{{ actor.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name:'ActorItem',
  props:{
    actor : Object,
  }
}
</script>

<style>
.actor-card{
  width: 180px;
  height: 260px;
  border-radius: 10px;
  overflow: hidden;
}
.actor-card-null{
  background-image: url('@/assets/Profile.png');
  background-position-x: -40px;
  background-position-y: 20px;
  background-size: 130%;


}
</style>