# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```


## Frontend - Vue

---

1. packages
   
   - axios
   - vue-router
   - vuex
   - vuex-persistedstate

2. Prototype
   
   - 디자인 툴 Figma를 이용하여 제작 https://www.figma.com/proto/fwA4fj5b36KaCumLDnD9YV/Film?type=design&node-id=5-2&scaling=min-zoom&page-id=0%3A1 링크
   - Figma를 처음 써봤는데 생각보다 틀만 구성하는데도 시간이 오래 걸렸다.
   - 그래도 한번 틀을 구성하니 이후에 컴포넌트와 뷰 구성이 편해졌다.

3. Reference
   
   - 인터넷에는 상상이상으로 많은 reference가 있어서 원하는 코드를 복사해 적당히 바꿔서 쓸 수 있는 점이 좋았습니다. 다만, 많은 복붙개발은 실력 향상에는 도움이 되지 않기 때문에 경계해야겠습니다.
   - carousel 컴포넌트, 별점 기능, 로그인폼, 깔끔한 체크박스 등을 인터넷에서 참고했습니다.

4. Clue : 영화 포스터 맞추기
   
   - 영화 포스터를 25등분하여 한 조각씩 보여주어 세 개의 선택지 중에서 영화 제목을 고르는 기능을 직접 만들었습니다.
   
   - background-image와 background-position, top, left 속성을 적절히 활용해 구현했습니다.
     
     ```css
     <div v-for="(hint, idx) in showHintList" :key="idx" class="quiz_hint"
       :style="`top: ${(img_size_y) * hint.offset_y}px; left: ${(img_size_x) * hint.offset_x}px;
       background-position : ${hint.offset_x * 100}% ${hint.offset_y * 100}%;
       background-image: url('${imageURL(randomMovie[0])}');`"></div>
     ```
   
   - 포스터마다 height 가 조금씩 달라 완벽하지는 않지만 css와 javascript로 퀴즈 기능을 만드니 재밌는 경험이었습니다.
     
     ![Untitled.png](./README_asset/Untitled.png)

5. 무분별한 Component 생성
   
   - 한번 쓰는 요소임에도 컴포넌트로 만들어 기능에 비해 많은 컴포넌트가 만들어졌습니다. 물론 기능별 코드의 길이가 짧아서 한눈에 보기는 편했습니다만 이 파일 저 파일 옮겨 다녀야 하니 불편했습니다. 앞으로는 여러 곳에서 사용할 요소가 아니면 컴포넌트로 만들어 사용하는 것을 자제해야겠습니다.


## 느낀점

### 이정훈

> 프로젝트 규모

- 싸피에서 가장 바쁘게 보낸 일주일이 아닌가 싶습니다. 프로젝트가 시작되니 생각보다 개발 속도가 빠르지 않았고 개발 진행 속도에 대한 감이 없다 보니 프로젝트 규모를 설정하는데 있어 어려움이 있었습니다. 스케일을 작게 잡아도 어느새 UI&UX 와 독창성을 생각하다 보니 어느새 프로젝트 규모가 커져 있었습니다. 다른 팀들의 프로젝트를 보며 승부욕에 더 그랬던 것 같습니다. 더 구현해보고 싶은 기능들이 있지만 이렇게 마무리 짓는 것이 아쉽습니다.

> 프로젝트 경험의 중요함

- 같이 팀을 이룬 정준우 님은 같은 알고리즘 스터디원이었기 때문에 친분이 있고 마음도 잘 맞아서 프로젝트가 순탄한 편이었지만, 서로 협업 경험이 적다 보니 상호 간에 소통이 적었습니다. 앞으로는 마음이 맞지 않는 팀원과도 협업 할 일은 많을 것이니 앞으로 있을 프로젝트에서 시행착오를 통해 의사소통 능력을 길러야겠습니다.

> 문제를 만나야 한다

- 개발 중에 사소한 에러에 시간을 잡아 먹히는 일이 많았습니다. 처음 보는 에러는 해결에 어려움이 있었고 겪었던 에러는 상대적으로 해결이 수월했습니다. 결국 에러는 경험 부족에서 나옴을 체감했습니다. 앞으로 있을 2학기 프로젝트에서 최대한 많은 문제를 경험해서 문제 해결능력을 기르고 싶습니다. 개발에 있어서 암기보다 경험이 중요한 것 같습니다.
