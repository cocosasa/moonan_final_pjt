# 🔎 Moonan : 영화 추천 & 해결 커뮤니티 사이트

---

> Moonan은 기본적으로 영화 추천 서비스를 제공하며 사용자 간 영화 관련 질문을 주고 받는 탐정 테마 영화 커뮤니티 사이트입니다.

> 이 영화 뭐지? 할 때 정보를 공유하며 궁금함을 해결할 수 있는 서비스

### Information

---

- 백엔드 & 조장 : 정준우
- 프론트엔드 : 이정훈
- 2023.05.16 ~ 2023.05.25 ( 10 days )

| 팀원  | 업무 내용                                                                    |
| --- | ------------------------------------------------------------------------ |
| 정준우 | 백엔드 - Django 모델 구성, fixture 제작, RESTful API 구성, CSS , 발표 자료              |
| 이정훈 | 프론트 엔드 - 프로토타입 제작, Vue 컴포넌트 관리 및 Vue Axios(로그인, front-back 연결), CSS , 발표 |

- Tool
  - Git - 프로젝트 소스코드 관리
  - Notion - 기획 회의 내용 기록 및 일일 작업 확인 체크 용도
  - Mattermost - 파일 전송 및 실시간 소통 용도
  - Figma - Prototype 제작
  - Sqlite3 - DataBase

### Installation

---

개발환경

- Django
  - v3.2.18
- Vue
  - Vue 2.6.14

Server setting

- django server
  
  ```bash
  cd backend
  pip install -r requirements.txt
  py manage.py makemigrations
  py manage.py migrate
  py manage.py loaddata movie_data.json actor_data.json genre_data.json recommend_data.json
  py manage.py runserver
  ```

- vue server
  
  ```bash
  cd frontend
  npm i
  npm run serve
  ```

### Description

---

- **Home.** 메인 페이지로 인기 영화의 포스터를 추천

- **Movie.** 인기순, 평점 순, 카테고리 별 영화 검색

- **Clue**. 영화 포스터 맞추기

- **Recommend.** 각 테마에 맞는 영화 리스트를 추천

- **Mongtage**. 영화 관련 질문 게시판

- **Search**. 영화 검색 기능

- **Profile**. 유저가 체크한 시청한 영화와 보고 싶은 영화 목록을 확인 가능하며 유저간 Follow 가능

- **Movie Detail**. 영화에 대한 상세 정보 확인, 한 줄평 작성

- 상세 명세서
  
  1. Home
     1. 인기 영화의 포스터를 Carousel을 이용해 보여주며, 자동으로 넘어가게 구현 - 누르면 상세 정보로
     2. 하단에 각 10개의 영화를 가진 추천 리스트들 중 일부를 무작위로 보여주며 또한 누르면 상세 정보로
  2. Movie
     1. 장르 카테고리를 선택해 고른 장르의 영화만 볼 수 있도록 구현
     2. 스크롤을 내리면 계속해서 영화 목록을 불러올 수 있도록 구현
     3. 다시 페이지 최상단으로 올라갈 수 있는 버튼 구현
     4. 각 영화의 포스터를 클릭하면 상세 정보로 갈 수 있도록 구현
  3. Clue
     1. DB내의 무작위 영화의 포스터의 일부를 보고 주어진 보기 중 알맞은 영화를 맞추는 게임 구현
     2. 포스터 조각을 하나씩 더 제공받을 때마다 맞췄을 시 얻을 점수 감소
     3. 정답을 맞추면 현재 로그인된 유저의 프로필 정보 중 Points 를 증가
  4. Recommend
     1. Home 처럼 추천 리스트 중 일부를 가져와 정보 제공
     2. 포스터를 클릭하면 해당 영화의 상세정보로 이동
  5. Community
     1. 알고 싶은 영화에 대해 이미지와 함께 내용을 올릴 수 있도록 구현
     2. 질문 글을 올릴 때 본인이 보유한 포인트 내에서 상금을 걸 수 있도록 구현
     3. 답변이 채택된다면 질문자가 걸어 놓은 포인트를 답변자가 가져가도록 구현
     4. 채택된 답변에 테두리를 만들어줘 어떤 답변이 정답인지 한 눈에 볼 수 있도록 구현
     5. 해결된 질문과 아닌 질문을 쉽게 구별할 수 있는 요소 추가
  6. Search
     1. 띄어쓰기를 통해 구분된 여러 요소를 한 번에 고려한 검색을 구현
  7. Login / Signup
     1. 따로 페이지를 만들지 않고 한 페이지에서 로그인과 회원가입 중 하나를 할 수 있도록 구현
  8. Profile
     1. 프로필 사진 기능 구현
     2. 보고 싶은 영화, 이미 본 영화 리스트 구현
     3. 팔로우 기능 구현
  9. Detail
     1. 각 영화의 상세 정보 제공
     2. 보고 싶은 영화, 이미 본 영화 리스트에 추가할 수 있는 기능 구현
     3. 예고편 제공
     4. 배우 목록 제공
     5. 영화에 대한 한 줄평과 별점 부여 기능 구현

> **ERD**

---

![ERD.png](./README_asset/ERD.png)

---

> **Commponent-Diagram**

---

![컴포넌트 다이어그램.png](./README_asset/%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%20%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.png)

---


### ScreenShot

---

### Logo

---

Moonan : 코난 + Movie

![logo](./README_asset/logo2.png)

![android-chrome-192x192.png](./README_asset/android-chrome-192x192.png)

---