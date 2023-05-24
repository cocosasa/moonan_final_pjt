<template>
  <div>
    <h1 class="text-center my-5">Challenge</h1>
    <h3 class="text-center my-sm-5" >{{currentScore}} 점</h3>
    <div class="quiz_img" v-if="randomMovie[0]"> 
        <div v-for="(hint, idx) in showHintList" :key="idx" class="quiz_hint" :style="`top: ${(img_size_y) * hint.offset_y}px; left: ${(img_size_x) * hint.offset_x}px; background-position : ${hint.offset_x * 100}% ${hint.offset_y * 100}%;background-image: url('${imageURL(randomMovie[0])}');`">
        </div>
    </div>
    <div class="d-flex justify-content-center gap-5 my-5">
      <button class="btn btn-outline-dark" @click="checkAnswer(0)">{{ randomMovie[selectionOrder[0]].title }}</button>
      <button class="btn btn-outline-dark" @click="checkAnswer(1)">{{ randomMovie[selectionOrder[1]].title }}</button>
      <button class="btn btn-outline-dark" @click="checkAnswer(2)">{{ randomMovie[selectionOrder[2]].title }}</button>
    </div>
    <div class="d-flex justify-content-end">
      <button @click="moreHint" v-if="nowHint < 25" class="btn btn-secondary">더 보기 -10점</button>
      <button v-else>더 보기 없음</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name :'ChallengeView',
  data(){
    return{
      currentScore : 250, 
      nowHint : 1, 
      img_size_x: 400,
      img_size_y: 600,
      hintList: [
        {
          offset_x: 0,
          offset_y: 0,
        },
        {
          offset_x: 0,
          offset_y: 0.25,
        },
        {
          offset_x: 0,
          offset_y: 0.5,
        },
        {
          offset_x: 0,
          offset_y: 0.75,
        },
        {
          offset_x: 0,
          offset_y: 1,
        },
        {
          offset_x: 0.25,
          offset_y: 0,
        },
        {
          offset_x: 0.25,
          offset_y: 0.25,
        },
        {
          offset_x: 0.25,
          offset_y: 0.5,
        },
        {
          offset_x: 0.25,
          offset_y: 0.75,
        },
        {
          offset_x: 0.25,
          offset_y: 1,
        },
        {
          offset_x: 0.50,
          offset_y: 0,
        },
        {
          offset_x: 0.50,
          offset_y: 0.25,
        },
        {
          offset_x: 0.50,
          offset_y: 0.5,
        },
        {
          offset_x: 0.50,
          offset_y: 0.75,
        },
        {
          offset_x: 0.50,
          offset_y: 1,
        },
        {
          offset_x: 0.75,
          offset_y: 0.0,
        },
        {
          offset_x: 0.75,
          offset_y: 0.25,
        },
        {
          offset_x: 0.75,
          offset_y: 0.5,
        },
        {
          offset_x: 0.75,
          offset_y: 0.75,
        },
        {
          offset_x: 0.75,
          offset_y: 1,
        },
        {
          offset_x: 1,
          offset_y: 0,
        },
        {
          offset_x: 1,
          offset_y: 0.25,
        },
        {
          offset_x: 1,
          offset_y: 0.5,
        },
        {
          offset_x: 1,
          offset_y: 0.75,
        },
        {
          offset_x: 1,
          offset_y: 1,
        },

      ],
      hint_size_x: 80,
      hint_size_y: 120,
      randomHintList: []
    }
  },
  created(){
    this.randomHints()
  },
  components : {
  },
  computed:{
    randomMovie () {
    return _.sampleSize(this.$store.state.popularMovieList,3)
    },
    showHintList (){
      return this.randomHintList.slice(0,this.nowHint)
    },
    selectionOrder(){
      return _.sampleSize([0,1,2], 3)
    }
  },
  methods:{
    imageURL(movie) {
      return 'https://image.tmdb.org/t/p/w500/' + movie.poster_path
    },
    randomHints() {
      this.randomHintList = _.sampleSize(this.hintList, 25)
    },
    moreHint(){
      if(this.nowHint < 25) {
        this.nowHint += 1
        this.currentScore -= 10
      }
      else{
        alert('아.. 누르지 마세요')
      }
    },
    checkAnswer(num){
      if(this.selectionOrder[num] == 0 ){
        axios({
          method: 'put',
          url: `${API_URL}/community/quiz/correct/${this.currentScore}/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            console.log(res.data)
            alert(`정답을 맞추셨습니다! ${this.currentScore} 포인트를 획득하셨습니다!`)
            this.$router.push({ name: 'main' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
      else{
        alert(`오답입니다. 정답은 ${this.randomMovie[0].title}입니다`)
      }
    }
  }
}
</script>

<style>
.quiz_img{
  margin: 0 auto;
  width: 480px;
  height: 760px;
  position: relative;
}
.quiz_hint{
  position: absolute;
  width: 100px;
  height: 150px;
}
</style>