<template>
  <div>
    <input @keyup.enter="searchMovie" type="text" v-model.trim="keyword">
    <button @click="searchMovie">search</button>
  </div>
</template>

<script>
export default {
  name:'SearchBar',
  date(){
    return {
      keyword : null,
    }
  },
  methods:{
    searchMovie(){
      if(!this.keyword){
        return
      }
      if(this.$router.currentRoute === 'search') {
        this.$router.replace({ name: 'search', params:{ keyword: this.keyword } })
      }
      else{
        this.$router.push({name:'search', params:{ keyword:this.keyword}})
      }
    }
  }
}
</script>

<style>

</style>