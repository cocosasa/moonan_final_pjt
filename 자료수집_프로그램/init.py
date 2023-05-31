import requests
import json

TMDB_API_KEY = 'db810f1ce85d6d911d7c5d0b9f259284'
Actorset = set()
Actors = []
def get_movie_datas():
    total_data = []

    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                video_request_url = f'https://api.themoviedb.org/3/movie/{movie["id"]}/videos?api_key={TMDB_API_KEY}&language=ko-KR'
                video_en_request_url = f'https://api.themoviedb.org/3/movie/{movie["id"]}/videos?api_key={TMDB_API_KEY}'


                credit_url = f'https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key={TMDB_API_KEY}'

                credits_result = requests.get(credit_url).json()
                
                actors = []

                for person in credits_result['cast'] :
                    if person['known_for_department'] == 'Acting':
                        # print(person["id"])
                        actors.append(person['id'])
                        fieldss = {
                            'name': person['name'],
                            'image_path': person['profile_path'],
                        }
                        Actors.append({
                            "pk": person['id'],
                            "model": "movies.actor",
                            "fields": fieldss
                        })
                        # if len(actors) >= 20 :
                        #     break
                

                videos = requests.get(video_request_url).json()
                selected_video = ''
                selected_video_name = ''
                keywords = ['파이널 예고편','파이널','최종 예고편','최종','3차 예고편','2차 예고편','1차 예고편','예고편','티저']
                # print(movie)
                keywords_en = ['Final Trailar', 'Final', 'FINAL','final', 'Official Trailar', 'Official', 'Trailar', 'TRAILAR', 'Teaser', 'TEASER']
                for keyword in keywords :
                    for video in videos['results'] :
                        if keyword in video["name"]  :
                            selected_video = video["key"]
                            selected_video_name = video["name"]
                    if selected_video :
                        break

                if not selected_video :
                    videos = requests.get(video_en_request_url).json()
                    for keyword in keywords_en :
                        for video in videos['results'] :
                            if keyword in video["name"]  :
                                selected_video = video["key"]
                                selected_video_name = video["name"]
                        if selected_video :
                            break
                if not selected_video and len(videos['results']):
                    selected_video = videos['results'][0]["key"]
                    selected_video_name = video["name"]
                # print(selected_video_name)
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'backdrop_path': movie['backdrop_path'],
                    'poster_path': movie['poster_path'],
                    'video_path': selected_video,
                    'actors': actors,
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)



def get_actor_data():
    total_data = []
    
    for actor in Actors:
        if actor['id'] in Actorset :
            print('f')
            continue
        fields = {
            # 'genre_id': genre['id'],
            'name': actor['name'],
            'popularity': actor['popularity'],
            'image_path': actor['profile_path'],
        }

        data = {
            "pk": actor['id'],
            "model": "movies.actor",
            "fields": fields
        }
        total_data.append(data)
        Actorset.add(actor['id'])

    with open("movies/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(Actors, w, indent=4, ensure_ascii=False)


get_movie_datas()
# get_genre_data()
# get_actor_data()
with open("movies/fixtures/actor_data.json", "w", encoding="utf-8") as w:
    json.dump(Actors, w, indent=4, ensure_ascii=False)
'''
movies/fixtures/ 만들고 

python init.py 

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json

'''