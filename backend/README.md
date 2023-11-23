
## Backend - Django

---

1. Home / Recommend
   
   메인 페이지나 추천 페이지에서 영화 리스트를 가져올 때 개별 영화 정보 내의 인기 / 평점을 이용해 두 가지 방식으로 정렬될 수 있도록 구현해야 했다.
   
   views는 python 파일로 만들어진다는 근거 하나로 받아온 Queryset을 리스트 형태로 바꾸고,
   
   popularity 나 vote_avg를 기준으로 정렬해 원하는 기능을 구현할 수 있었다.
   
   Django 과정 중 배운 것 뿐만 아니라 python의 기초적인 지식도 결합해 문제를 해결할 수 있다는 것을
   
   학습한 과정이었다.

2. Movie
   
   영화 정보, 장르, 배우, 추천 리스트 등 다양한 정보가 필요해서 적절한 Json 파일을 만들 필요가 있었다.
   
   ```python
   def get_movie_datas():
       total_data = []
   
       for i in range(1, 10):
           request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&include_adult=false&language=ko-KR&page={i}"
           movies = requests.get(request_url).json()
   
           for movie in movies['results']:
               if movie.get('release_date', ''):
                   fields = {
                       # 'movie_id': movie['id'],
                       'title': movie['title'],
                       'released_date': movie['release_date'],
                       'popularity': movie['popularity'],
                       'vote_avg': movie['vote_average'],
                       'overview': movie['overview'],
                       'poster_path': movie['poster_path'],
                       'genres': movie['genre_ids'],
                   }
   
                   data = {
                       "pk": movie['id'],
                       "model": "movies.movie",
                       "fields": fields
                   }
   
                   total_data.append(data)
   
       with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
           json.dump(total_data, w, indent=4, ensure_ascii=False)
   ```
   
   위 코드는 영화 데이터 중 지정한 필드의 요소만을 가져와 Json 파일로 만들어주는 것으로,
   
   위 코드를 기반으로 정보를 수정해 필요한 자료들을 모두 얻어낼 수 있었다.
   
   그 중 배우 데이터는 따로 제공되지 않아 특정 영화의 크레딧을 추출 할 수 있는 TMDB API를 통해
   
   갖고 있는 영화들의 모든 크레딧 중, 역할이 ‘Acting’인 사람들을 따로 추출해 DB에 있는 영화들에 한정해
   
   모든 배우들의 목록을 얻어낼 수 있었다.
   
   복잡하고 코드 실행 시간도 오래 걸리는 과정이긴 했지만, 데이터 간의 연관성을 파악하고 필요한 정보를
   
   얻어낼 수 있는 역량을 기를 수 있는 과정이었다 생각한다.

3. Clue
   
   ```python
   @api_view(['PUT'])
   @permission_classes([IsAuthenticated])
   def choose_answer(request, points_get):
       me = get_object_or_404(Profile, user = request.user)
       serializer = ProfileSerializer(me, data = request.data)
       if serializer.is_valid(raise_exception = True):
           serializer.save(points = me.points + points_get)
           return Response(status = status.HTTP_200_OK)
   ```
   
   정답을 맞추면 현재 로그인된 계정의 포인트를 증가시켜주는 함수다.
   
   ```python
   class Profile(models.Model):
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
       points = models.IntegerField(default = 500)
       want_to_see_movies = models.ManyToManyField('movies.Movie', related_name = 'wants_users')
       watched_movies = models.ManyToManyField('movies.Movie', related_name = 'watches_users')
       profile_image = models.ImageField(null = True)
   ```
   
   포인트 필드가 들어있는 프로필 모델이다.
   
   가입하자마자 기본 포인트를 제공해주고 싶어 프로필 생성 후 포인트를 추가해주는 방법을 생각했지만,
   
   할 수는 있을 것 같아도 복잡해 구현이 쉽지 않았다.
   
   모델을 지정해줄 때 default를 통해 초기값을 정해줄 수 있다는 것을 알게 되었고, 이를 활용해
   
   기본 포인트 제공을 너무 간단하게 구현할 수 있었다.
   
   이외의 부분들은 Django 학습 과정 중 배운 것을 통해서 무난하게 구현할 수 있었지만,
   
   이는 Profile 모델에서 직접 넣어줘야 하는 부분이 포인트 뿐이라 그랬던 것임을 이후 과정에서 알게 되었다.

4. Community
   
   ```python
   @api_view(['GET', 'POST'])
   @permission_classes([IsAuthenticated])
   def create_question(request):
       serializer = QuestionSerializer(data = request.data)
   
       me = get_object_or_404(Profile, user = request.user)
   
       if me.points < int(serializer.initial_data['points']):
           return Response(status = status.HTTP_400_BAD_REQUEST)
   
       serializer2 = ProfileSerializer(me, data=request.data)
   
       if serializer.is_valid(raise_exception = True):
           serializer.save(user = request.user)
   
           if serializer2.is_valid(raise_exception = True):
               serializer2.save(points = me.points - serializer.data['points'])
   
               return Response(serializer.data, status = status.HTTP_201_CREATED)
   ```
   
   질문글에서 구현해야 할 첫 기능은 질문을 생성할 때 사용자가 입력한 숫자만큼 포인트를 차감하는 것이었다.
   
   처음에는 serializer2 부분만 있었는데, 아무 숫자나 입력해보다가 사용자가 보유한 포인트보다 더 큰 포인트를
   
   상금으로 걸 수 있다는 것을 알게 되었다.
   
   하지만 기존에 알던 방식으로는 serializer의 유효성 검사가 수행되기 전에 포인트를 가져와 입력값과 비교할 수가 없었다.
   
   serializer.initial_data[’field’] 를 통해 유효성 검사가 이루어지기 전에 field값을 가져와 사용할 수 있었고,
   
   이를 통해 글이 작성되기 전 적절한 포인트를 갖고 있는지 확인할 수 있게 되었다.
   
   ```python
   @api_view(['PUT'])
   @permission_classes([IsAuthenticated])
   def select_comment(request, question_pk, comment_pk):
       question = get_object_or_404(Question, pk = question_pk)
       if question.is_completed == False:
           if request.user == question.user:
               comment = get_object_or_404(QuestionComment, pk = comment_pk)
               answerer = get_object_or_404(Profile, user = comment.user)
               serializer = ProfileSerializer(answerer, data = request.data)
               if serializer.is_valid(raise_exception = True):
                   serializer.save(points = answerer.points + question.points)
   
                   serializer2 = QuestionSerializer(question, data = request.data, partial = True)
                   if serializer2.is_valid(raise_exception = True):
                       serializer2.save(is_completed = True)
   
                       serializer3 = QuestionCommentSerializer(comment, data = request.data, partial = True)
                       if serializer3.is_valid(raise_exception = True):
                           serializer3.save(is_chosen = True)
                   return Response(status = status.HTTP_200_OK)
       return Response(status = status.HTTP_401_UNAUTHORIZED)
   ```
   
   질문이 채택되었을 때 포인트를 제공하고 질문을 해결 상태로 바꾸며, 채택된 답변을 특정할 수 있도록 구현해야 했다.
   
   Clue 페이지에서 바뀐 포인트의 값만 주면 문제 없이 구현되었던 것과는 달리, 이번 단계에서는
   
   is_completed나 is_chosen 값만 바꾸려고 하니 나머지 값들도 제공해야만 한다고 해 함수가 실행되지 않았다.
   
   serializer 지정 과정에서 partial = True 조건을 부여해주면 serializer의 일부분만 변경할 수 있다는 것을 알게 되었고, 이를 통해 필요한 기능들을 모두 구현할 수 있었다.

5. Search
   
   ```python
   @api_view(['GET'])
   def movie_search(request, search):
       for word in search.split():
           movies = Movie.objects.filter(Q(title__icontains = word) | Q(overview__icontains = word) | Q(genres__name__icontains = word))
           searched_movies = []
           for movie in list(movies):
                   if movie not in searched_movies:
                       searched_movies.append(movie)
       searched_movies.sort(key = lambda x : x.popularity, reverse = True)
       serializer = MovieListSerializer(searched_movies, many = True)
       return Response(serializer.data)
   ```
   
   검색 단어를 띄어쓰기를 기준으로 나누고, 나눈 요소 하나하나를
   
   filter-Q와 icontains를 통해 제목 / 줄거리 / 장르 중 하나라도 포함되어 있다면
   
   해당 영화가 결과로 출력될 수 있도록 했다.
   
   Q는 Django model ORM 으로 where절에 or, and, not 조건을 부여해주고 싶을 때 사용된다.
   
   icontains는 같이 입력해준 문자열을 포함한 요소를 찾아주는 명령어로,
   
   대소분자를 구분하는 contains와 달리 대소문자를 구분하지 않아 더 다양한 검색 결과를 얻을 수 있다.

6. Profile
   
   ```python
   @api_view(['GET', 'PUT'])
   def profile(request, username) :
       user = get_object_or_404(get_user_model(), username = username)
       profile = get_object_or_404(Profile, pk = user.id)
       if request.method == 'GET' :
           serializer = ProfileSerializer(profile)
           return Response(serializer.data)
   
       elif request.method == 'PUT':
           if request.user == profile.user:
               serializer = ProfileSerializer(profile, data=request.data)
               if serializer.is_valid(raise_exception = True):
                   serializer.save()
                   return Response(serializer.data)
           return Response(status = status.HTTP_401_UNAUTHORIZED)
   ```
   
   프로필과 유저를 연결시켜주기 위해, 처음으로 오브젝트를 두개 이상 가져와 사용해봤다.
   
   username을 통해 특정 유저의 데이터를 가져오고 그것을 통해 해당 유저의 프로필과 연결해
   
   데이터를 가져오거나 수정할 수 있도록 구현했다.

7. Detail
   
   ```python
   @api_view(['POST'])
   @permission_classes([IsAuthenticated])
   def wanted(request, movie_pk):
       me = get_object_or_404(Profile, pk = request.user.pk)
       movie = get_object_or_404(Movie, pk = movie_pk)
   
       if me.want_to_see_movies.filter(pk = movie_pk).exists():
           me.want_to_see_movies.remove(movie)
           wanted = False
       else:
           me.want_to_see_movies.add(movie)
           wanted = True
   
           if me.watched_movies.filter(pk = movie_pk).exists():
               me.watched_movies.remove(movie)
               is_watched = False
   
       serializer = ProfileSerializer(me)
       return Response(serializer.data)
   
   @api_view(['POST'])
   @permission_classes([IsAuthenticated])
   def watched(request, movie_pk):
       me = get_object_or_404(Profile, pk = request.user.pk)
       movie = get_object_or_404(Movie, pk = movie_pk)
   
       if me.watched_movies.filter(pk = movie_pk).exists():
           me.watched_movies.remove(movie)
           watched = False
   
       else:
           me.watched_movies.add(movie)
           watched = True
   
           if me.want_to_see_movies.filter(pk = movie_pk).exists():
               me.want_to_see_movies.remove(movie)
               wanted = False
   
       serializer = ProfileSerializer(me)
       return Response(serializer.data)
   ```
   
   위의 프로필에서 구현했던 것과 마찬가지로, 두 개의 오브젝트를 가져와 사용했다.
   
   요청한 사용자의 데이터에서 pk를 가져오고, 현재 보고 있는 영화 상세 페이지의 정보를 이용해 영화 id를 가져와
   
   이미 리스트에 있다면 삭제하고 아니라면 추가하는 식으로 wanted와 watched 모두 구현했다.
   
   두 가지가 같이 체크 되어 있을 수 없기 때문에 한 쪽 함수가 실행되었을 때 다른 쪽도 살펴보며
   
   동시에 활성화되지 않게 조치했다.
   
   ```python
   class ReviewCommentSerializer(serializers.ModelSerializer):
       child_comments = serializers.PrimaryKeyRelatedField(many = True, read_only = True, allow_null = True)
   
       class Meta:
           model = ReviewComment
           fields = ('id', 'review', 'content', 'user', 'created_at', 'updated_at', 'parent_comment', 'child_comments')
           read_only_fields = ('user', 'review', 'parent_comment')
   ```
   
   대댓글 기능 구현을 위해 자식 댓글의 정보를 얻을 수 있도록 serializer를 구성했다.
   
   ```python
   @api_view(['POST'])
   @permission_classes([IsAuthenticated])
   def create_review_comment(request, review_pk):
       review = get_object_or_404(Review, pk = review_pk)
       serializer = ReviewCommentSerializer(data = request.data)
   
       if serializer.is_valid(raise_exception = True):
           serializer.save(user = request.user, review = review)
           return Response(serializer.data, status = status.HTTP_201_CREATED)
   
   # 대댓글
   @api_view(['POST'])
   @permission_classes([IsAuthenticated])
   def review_ccomment_create(request, comment_pk):
       comment = get_object_or_404(ReviewComment, pk = comment_pk)
       serializer = ReviewCommentSerializer(data = request.data)
   
       if serializer.is_valid(raise_exception = True):
           serializer.save(user = request.user, parent_comment = comment)
           return Response(serializer.data, status = status.HTTP_201_CREATED)
   ```
   
   댓글과 대댓글의 함수는 따로 구분했고, 댓글을 추가하는 과정은 같지만 해당 댓글이 추가되는 곳이
   
   리뷰인지, 다른 댓글인지에 따라 오브젝트를 다르게 가져와 구현했다.
   
   ***

   
## 느낀점

### 정준우

> 진짜 최종 프로젝트

- 최종 프로젝트인만큼, 초반에 학습했던 내용에서부터 후반부 내용까지 모든 걸 사용해서야 하나의 서비스를 구현할 수 있었다. 완벽히 학습되지 않아 단편적인 기억들을 더듬어 대부분 검색 과정을 한 번은 거치고 나서야 코드로 적어나갈 수 있었다. 하지만 “여기에 쓸만한 이런 게 있었던 것 같은데?” 하는 생각이 들어서 이리저리 자료를 찾아보면 해당 내용이 금방 나와 코드에 적용할 수 있었고, 그 과정에서 더 나아가 더 효율적으로 같은 기능을 구현할 수 있는 방법을 찾는 경우도 자주 있었다.

> 일단 해보는 것

- 완벽히 이해하지 못한 지식이라도 우선 학습하고 경험해두면 다시 그 내용을 알아봐야 할 때 기반이 없는 것보다는 훨씬 효율적인 과정을 거칠 수 있다는 것을 확실히 깨달은 프로젝트였고, 현재 python 하나도 완벽히 다루지 못하는 상황에서 취업 시장의 분위기에 맞춰 Java를 공부해야 할지 말지 고민하던 상황에서 일단 python으로 프로그래밍 경험을 쌓았으니 두 언어를 모두 공부해나가며 “업무에서 써 보진 않았지만 쓸 줄은 압니다” 라도 말할 수 있도록 해야겠다는 결심을 할 수 있게 한 프로젝트였다.
