<template>
  <div class="border rounded-5 overflow-hidden ps-3 pe-1 py-0 d-flex bg-white" :class="{'border-danger':isSearching}">
    <input class="border-0 search-bar-inputbox p-2 bg-white text-start" @keyup.enter="searchMovie" type="text" v-model.trim="keyword">
    <button class="search-bar-btn" @click="searchMovie"><i class="fa-solid fa-magnifying-glass fa-lg" style="color: black;"></i></button>
  </div>
</template>

<script>
export default {
  name:'SearchBar',
  data(){
    return {
      keyword : null,
    }
  },
  computed:{
    isSearching(){
      return this.$router.currentRoute === 'search'
    }
  },
  methods:{
    searchMovie(){
      if(!this.keyword){
        return
      }
      if(this.isSearching) {
        this.$router.replace({ name: 'search', params:{ keyword: this.keyword } })
      }
      else{
        this.$router.push({name:'search', params:{ keyword: this.keyword }}).catch(() => { });
      }
    }
  }
}
</script>

<style>
.search-bar-inputbox:focus{
  outline: none;
}
.search-bar-btn{
  outline: none;
  background-color: white;
  border: 0px;
}
</style>