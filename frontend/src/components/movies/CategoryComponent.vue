<template>
  <div class="d-flex flex-wrap justify-content-start mt-4">
    <!-- <div v-for="genre in genreList" :key="genre.id" class="btn p-2 px-3 rounded-5 border me-1 mb-2" :class="{'btn-primary':selectedGenre.includes(genre.name)}"> -->
      <input v-for="genre in genreList" :key="genre.id" class="btn p-2 px-3 me-2 mb-2 checkbox" type="checkbox" :value="genre.name" :id="genre.id" v-model="selectedGenre" @click="check">
    <!-- </div> -->
    <!-- <button class="ms-5 btn-dark btn rounded-5 py-1">검색</button> -->
  </div>
</template>

<script>

export default {
  name:'CategoryComponent',
  created(){
  },
  data(){
    return{
      selectedGenre : []
    }
  },
  computed:{
    genreList(){
      return this.$store.state.genreList
    }
  },
  methods:{
    check(){
      setTimeout(()=>{
        this.searchGenre()
      }, 50)
      
    },
    searchGenre(){
      this.$emit('search-genre', this.selectedGenre)
    }
  }
}
</script>

<style>
.checkbox {
  appearance: none;
  height: 30px;
  width: 140px;
  border-radius: 15px;
  /* background-image: radial-gradient(
    circle farthest-corner at 10% 20%,
    rgba(37, 145, 251, 0.98) 0.1%,
    rgba(0, 7, 128, 1) 99.8%
  ); */
  background-color: red;
  background-size: 360% 100%;
  /* border-radius: 50px; */
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.checkbox:after {
  content: attr(value);
  word-break: keep-all;
  top: 50%;
  position: absolute;
  /* left: 30%; */
  transform: translate(-50%, -50%);
  font-size: 16px;
  font-family: "Inter", sans-serif;
  color: #000000;
  /* z-index: 99; */
  transition: all 0.2s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.checkbox:before {
  content: "";
  position: absolute;
  top: 0%;
  left: 0px;
  height: 300%;
  width: 200%;
  background: #ffffff;
  z-index: 0;
  transition: all 0.2s linear;
  transform: scale(0.5) translate(-50%, -85%);
}
.checkbox:hover:before,
.checkbox:focus-visible:before {
  background: #ffffffec;
  top: -4%;
  left: 20%;
}
.checkbox:checked:before {
  top: -100%;
}
.checkbox:checked:after {
  color: rgb(255, 255, 255);
  
}
.checkbox:checked {
  box-shadow: 0px 2px 5px -3px black;
}

.checkbox:focus-visible {
  outline: none;
  box-shadow: 0px 0px 0px 5px #480f5d;
}
</style>