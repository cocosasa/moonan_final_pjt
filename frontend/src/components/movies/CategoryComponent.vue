<template>
  <div class="d-flex flex-wrap justify-content-start my-4" id="to-top">
      <input v-for="genre in genreList" :key="genre.id" class="btn p-2 px-3 mb-2 checkbox fw-bold" type="checkbox" :value="genre.name" :id="genre.id" v-model="selectedGenre" @click="check">
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
  width: 124px;
  margin-right: 9px;
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
.checkbox:last-child{
  margin-right: 0px;
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
  top: 50%;
  left: -50%;
  height: 300%;
  width: 300%;
  background: #ffffff;
  z-index: 0;
  transition: all 0.2s ease-out;
  transform: scale(0.5) translate(-50%, -100%);
}
.checkbox:hover:before,
.checkbox:focus-visible:before {
  background: #ffffffec;
  top: 50%;
  left: -50%;
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