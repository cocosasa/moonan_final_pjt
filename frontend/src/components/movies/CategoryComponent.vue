<template>
  <div class="d-flex">
    <div v-for="genre in genreList" :key="genre.id" >
      <label :for="genre.name">{{ genre.name }}</label>
      <input type="checkbox" :name="genre.name" :id="genre.id">
    </div>
  </div>
</template>

<script>

export default {
  name:'CategoryComponent',
  created(){
  },
  computed:{
    genreList(){
      return this.$store.state.genreList
    }
  }
}
</script>

<style>

</style>