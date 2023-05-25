<template>
  <div>
    <h1 class="text-center my-5"><span class = "bold color-change" style = "font-size: 60px">Poster Challenge</span></h1>
    <h5 class = "text-center" style = "font-size: 20px">포스터 일부를 보고 영화를 맞혀보세요!</h5>
    <h3 class="text-center my-sm-5 bold over-underline" v-if="currentScore != 0">정답 맞힐 시 {{currentScore}}점 획득</h3>
    <h3 class="text-center my-sm-5" v-if="currentScore == 0">{{ randomMovie[0].title }}</h3>
    <div class="quiz_img" v-if="randomMovie[0]"> 
        <div v-for="(hint, idx) in showHintList" :key="idx" class="quiz_hint" :style="`top: ${(img_size_y) * hint.offset_y}px; left: ${(img_size_x) * hint.offset_x}px; background-position : ${hint.offset_x * 100}% ${hint.offset_y * 100}%;background-image: url('${imageURL(randomMovie[0])}');`">
        </div>
    </div>
    <div class="d-flex justify-content-center gap-5 my-5" v-if="currentScore!=0">
      <button class="btn btn-outline-dark option" @click="checkAnswer(0)">{{ randomMovie[selectionOrder[0]].title }}</button>
      <button class="btn btn-outline-dark option" @click="checkAnswer(1)">{{ randomMovie[selectionOrder[1]].title }}</button>
      <button class="btn btn-outline-dark option" @click="checkAnswer(2)">{{ randomMovie[selectionOrder[2]].title }}</button>
    </div>
    <div class="d-flex justify-content-center" v-if="currentScore != 0">
      <button @click="moreHint" class="btn btn-secondary"><span v-if="nowHint < 25">더보기 -10 점</span> <span v-if="nowHint == 25">더보기 없음</span></button>
    </div>
    <div v-if="currentScore == 0" class="d-flex justify-content-center gap-5 my-5">
      <button @click="nextMovie" class = "btn btn-secondary" id = "next">다음 문제</button>
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
      randomHintList: [],
      randomMovie : [],
      selectionOrder : [],
    }
  },
  created(){
    this.randomHints()
    this.nextMovie()
  },
  components : {
  },
  computed:{
    showHintList (){
      return this.randomHintList.slice(0,this.nowHint)
    },
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
            this.nowHint = 25
            this.currentScore = 0
            // this.$router.push({ name: 'main' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
      else{
        alert(`오답입니다. 정답은 ${this.randomMovie[0].title}입니다`)
        this.nowHint = 25
        this.currentScore = 0
      }
    },
    nextMovie(){
      this.nowHint = 1
      this.currentScore = 250
      this.randomMovie =  _.sampleSize(this.$store.state.popularMovieList, 3)
      this.selectionOrder = _.sampleSize([0, 1, 2], 3)
      this.randomHints()
    }
  }
}

</script>

<style>
html {
  background-color: #282828;
}
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
.bold{
  font-weight: bold;
}
.option{
  color: white;
  font-weight: bold;
  font-size: 20px;
}
.color-change{
  color: white;
  animation: ct 6s infinite;
}
@keyframes ct {
  25% {color: #b4b4b4;}
  50% {color: #828282;}
  75% {color: #505050;}
}
.over-underline {
  text-decoration-line: underline overline;
  text-decoration-thickness: 5px;
}
</style>