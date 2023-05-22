<template>
  <div>
    <iframe :src="videoURL" width="1120" height="630" frameborder="0" allowfullscreen allow="autoplay;" ></iframe>
    <h2>{{video?.snippet.title}}</h2>
    <p>{{video?.snippet.description}}</p>
  </div>
</template>

<script>
import axios from 'axios';

const API_KEY = 'AIzaSyDQc4qTtkuO7RXleZ_4FNSWh9jcunRBOVk'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const BASE_URL = 'https://www.youtube.com/embed/'
export default {
  name: 'MovieVideo',
  props : {
    movie : String,
  },
  data (){
    return {
      video : null
    }
  },
  created(){
    // console.log(this.movie)
    this.searchVideo(this.movie)
  },
  computed:{
    videoURL () {
      return `${BASE_URL}${this.video?.id.videoId}`
    }
  },
  methods:{
    searchVideo(keyword) {
      // console.log(keyword)
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: keyword,
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res => {
          console.log(res.data)
          this.video = res.data.items[0]
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
// {
//     "kind": "youtube#searchListResponse",
//     "etag": "Cp3Ik7WpC4exu-QtPnyPcvTLxrU",
//     "nextPageToken": "CAUQAA",
//     "regionCode": "KR",
//     "pageInfo": {
//         "totalResults": 3896,
//         "resultsPerPage": 5
//     },
//     "items": [
//         {
//             "kind": "youtube#searchResult",
//             "etag": "wvZFNiDSfXEUTQsSxhjq4w4_osE",
//             "id": {
//                 "kind": "youtube#video",
//                 "videoId": "Cr-Kj9MnTy4"
//             },
//             "snippet": {
//                 "publishedAt": "2023-05-04T06:27:23Z",
//                 "channelId": "UC_XI3ByFO1uZIIH-g-zJZiw",
//                 "title": "[다시보기] SSAFY 10기 온라인 모집설명회, 랜선 대격돌",
//                 "description": "지원서 제출 마감임박 5월8일(월) 17시까지!! 라면물이 끓는 5분이면 지원서 작성 완료! 지원서 제출하고 어버이날에 부모님께 효도 ...",
//                 "thumbnails": {
//                     "default": {
//                         "url": "https://i.ytimg.com/vi/Cr-Kj9MnTy4/default.jpg",
//                         "width": 120,
//                         "height": 90
//                     },
//                     "medium": {
//                         "url": "https://i.ytimg.com/vi/Cr-Kj9MnTy4/mqdefault.jpg",
//                         "width": 320,
//                         "height": 180
//                     },
//                     "high": {
//                         "url": "https://i.ytimg.com/vi/Cr-Kj9MnTy4/hqdefault.jpg",
//                         "width": 480,
//                         "height": 360
//                     }
//                 },
//                 "channelTitle": "삼성청년SW아카데미 Youtube채널 HELLOSSAFY",
//                 "liveBroadcastContent": "none",
//                 "publishTime": "2023-05-04T06:27:23Z"
//             }
//         },
//         {
//             "kind": "youtube#searchResult",
//             "etag": "Z65sM3bYFBs9H2ecFL7JEDCBAhA",
//             "id": {
//                 "kind": "youtube#video",
//                 "videoId": "kbZsqssYDl0"
//             },
//             "snippet": {
//                 "publishedAt": "2022-08-31T10:12:07Z",
//                 "channelId": "UCqPjSHRA0KB4TObEa2k0cRg",
//                 "title": "SSAFY| 싸피 8기가 말해주는 싸피 생활의 모든 것! | 싸밥, 커리큘럼, 수업난이도, 반 분위기 등 || SSAFYcial",
//                 "description": "안녕하세요, 재이입니다~ 오늘은 평소에 업로드하던 브이로그와는 다른 영상으로 찾아왔어요! 오늘 영상은 싸피의 공식 기자단인 '싸 ...",
//                 "thumbnails": {
//                     "default": {
//                         "url": "https://i.ytimg.com/vi/kbZsqssYDl0/default.jpg",
//                         "width": 120,
//                         "height": 90
//                     },
//                     "medium": {
//                         "url": "https://i.ytimg.com/vi/kbZsqssYDl0/mqdefault.jpg",
//                         "width": 320,
//                         "height": 180
//                     },
//                     "high": {
//                         "url": "https://i.ytimg.com/vi/kbZsqssYDl0/hqdefault.jpg",
//                         "width": 480,
//                         "height": 360
//                     }
//                 },
//                 "channelTitle": "재이의날들 daysofjayla",
//                 "liveBroadcastContent": "none",
//                 "publishTime": "2022-08-31T10:12:07Z"
//             }
//         },
//         {
//             "kind": "youtube#searchResult",
//             "etag": "0vCn0-FCt0dbdahQ_6rqs0dDnkM",
//             "id": {
//                 "kind": "youtube#video",
//                 "videoId": "kSpJUgAUme8"
//             },
//             "snippet": {
//                 "publishedAt": "2023-03-07T15:00:37Z",
//                 "channelId": "UCoN1XLeAX2OazuZdQ9b8U9Q",
//                 "title": "삼성의 부트캠프 SSAFY 리뷰",
//                 "description": "CS지식의 정석 https://inf.run/17Fb ▷C++ 10주완성 코딩테스트 https://inf.run/xZhA.",
//                 "thumbnails": {
//                     "default": {
//                         "url": "https://i.ytimg.com/vi/kSpJUgAUme8/default.jpg",
//                         "width": 120,
//                         "height": 90
//                     },
//                     "medium": {
//                         "url": "https://i.ytimg.com/vi/kSpJUgAUme8/mqdefault.jpg",
//                         "width": 320,
//                         "height": 180
//                     },
//                     "high": {
//                         "url": "https://i.ytimg.com/vi/kSpJUgAUme8/hqdefault.jpg",
//                         "width": 480,
//                         "height": 360
//                     }
//                 },
//                 "channelTitle": "큰돌의터전",
//                 "liveBroadcastContent": "none",
//                 "publishTime": "2023-03-07T15:00:37Z"
//             }
//         },
//         {
//             "kind": "youtube#searchResult",
//             "etag": "V0WayLfS7fyetL8tNU-hPS4Pc3Q",
//             "id": {
//                 "kind": "youtube#video",
//                 "videoId": "CgKUIHw2lHc"
//             },
//             "snippet": {
//                 "publishedAt": "2021-10-07T14:58:24Z",
//                 "channelId": "UCm4Fr2-8fuPnmjIyT6OfS0A",
//                 "title": "SSAFY(싸피) 쉽게 합격했던 방법 + 후기",
//                 "description": "제 개인적인 의견일 뿐입니다. 저는 이렇게 해서 합격했다구요... 개발자 지망생 분들 화이팅하세욥...",
//                 "thumbnails": {
//                     "default": {
//                         "url": "https://i.ytimg.com/vi/CgKUIHw2lHc/default.jpg",
//                         "width": 120,
//                         "height": 90
//                     },
//                     "medium": {
//                         "url": "https://i.ytimg.com/vi/CgKUIHw2lHc/mqdefault.jpg",
//                         "width": 320,
//                         "height": 180
//                     },
//                     "high": {
//                         "url": "https://i.ytimg.com/vi/CgKUIHw2lHc/hqdefault.jpg",
//                         "width": 480,
//                         "height": 360
//                     }
//                 },
//                 "channelTitle": "개발자 지름길",
//                 "liveBroadcastContent": "none",
//                 "publishTime": "2021-10-07T14:58:24Z"
//             }
//         },
//         {
//             "kind": "youtube#searchResult",
//             "etag": "-DsoamcuemCmIprYmHAMzTpXg-o",
//             "id": {
//                 "kind": "youtube#video",
//                 "videoId": "mKKbO_QTFVY"
//             },
//             "snippet": {
//                 "publishedAt": "2022-10-28T01:21:19Z",
//                 "channelId": "UCqPjSHRA0KB4TObEa2k0cRg",
//                 "title": "SSAFY 8기가 알려주는 싸피 합격 팁 총집합! (feat. 리얼 생생 후기) | 9기 지원자 다 드루와 | SSAFYcial",
//                 "description": "SSAFY 지원하러가기 ▷ https://bit.ly/3ffUB8K 안녕하세요, 재이입니다~ 오늘 영상은 싸피의 공식 기자단인 '싸피셜 (SSAFYcial)' 기자 ...",
//                 "thumbnails": {
//                     "default": {
//                         "url": "https://i.ytimg.com/vi/mKKbO_QTFVY/default.jpg",
//                         "width": 120,
//                         "height": 90
//                     },
//                     "medium": {
//                         "url": "https://i.ytimg.com/vi/mKKbO_QTFVY/mqdefault.jpg",
//                         "width": 320,
//                         "height": 180
//                     },
//                     "high": {
//                         "url": "https://i.ytimg.com/vi/mKKbO_QTFVY/hqdefault.jpg",
//                         "width": 480,
//                         "height": 360
//                     }
//                 },
//                 "channelTitle": "재이의날들 daysofjayla",
//                 "liveBroadcastContent": "none",
//                 "publishTime": "2022-10-28T01:21:19Z"
//             }
//         }
//     ]
// }