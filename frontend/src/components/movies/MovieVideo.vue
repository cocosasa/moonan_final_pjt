<template>
  <div class="my-3">
    <!-- <h2>{{video?.name}}</h2> -->
    <iframe v-if="video" :src="videoURL" width="1200" height="700" frameborder="0" autohide=1 allowfullscreen autoplay=1 showinfo=0 allow="autoplay;" ></iframe>
  </div>
</template>

<script>
import axios from 'axios';

const API_KEY = 'd89c572f2beb19860083c76dd212cabd'
const API_URL = 'https://api.themoviedb.org/3/movie'
const BASE_URL = 'https://www.youtube.com/embed/'
export default {
  name: 'MovieVideo',
  props : {
    movie : Object,
  },
  data (){
    return {
      video : null
    }
  },
  created(){
    this.searchVideo()
  },
  computed:{
    videoURL () {
      return BASE_URL + this.video?.key
    }
  },
  methods:{
    searchVideo() {
      let params = {
        api_key: API_KEY,
        language: 'ko-KR',
      }
      axios({
        method: 'get',
        url: `${API_URL}/${this.movie.id}/videos`,
        params,
      })
      .then(res => {
        console.log(res.data)
        if(res.data.results.length){
          res.data.results.forEach(el=>{
            if(el.name.includes('예고')){
              this.video = el
            }
          })
          if (this.video === null) {
            this.video = res.data.results[0]
          }
        }
        else {
          params = {
            api_key: API_KEY,
          }
          axios({
            method: 'get',
            url: `${API_URL}/${this.movie.id}/videos`,
            params,
          })
          .then(res=>{
            console.log(res.data)
            if (res.data.results.length) {
              res.data.results.forEach(el => {
                if (el.name.includes('Trailer')) {
                  this.video = el
                }
              })
              if(this.video === null){
                this.video = res.data.results[0]
              }
            }
          })
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>
