import json

from django.http import JsonResponse
from django.views import View

from movie.models import Actor, Movie, ActorMovie

class ActorView(View):
# http -v GET  http://127.0.0.1:8000/movie/actor
    def get(self, request):
        try:
            actors = Actor.objects.all()
            result = []
            for actor in actors:
                #이걸 왜 하냐면, 배우1에 해당하는 출연작 모두의 모든 정보를 가진
                #객체..?가 여러개 나오는거니까 -> 얘는 쿼리셋이쟈나 
                movies = actor.movie.all()
                movie_list=[]
                for movie in movies:
                    movie_list.append(movie)
                result.append(
                        {
                            'first_name'    : actor.first_name,
                            'last_name'     : actor.last_name,
                            'date_of_birth' : actor.date_of_birth,
                            'movie'         : movie_list
                        }
                    )
            return JsonResponse({'result': result}, status = 200)
        
        except Exception:
            return JsonResponse({'result':'key_error'}, status = 400)
        
    def post(self, request):
        try:
            data = json.loads(request.body)
            Actor.objects.create(
                first_name = data['first_name'],
                last_name  = data['last_name'],
                date_of_birth = data['date_of_birth']
            )
            return JsonResponse({'result':'created'}, status = 201)
        
        except KeyError:
            return JsonResponse({'result':'key_error'}, status = 400)
        except TypeError:
            return JsonResponse({'result':'type_error'}, status = 400)
        
class MovieView(View):
    # http -v GET  http://127.0.0.1:8000/movie
    def get(self, request):
        try:
            movies = Movie.objects.all()
            result = []
            for movie in movies:    
                result.append(
                    {
                        'title'        : movie.title, 
                        'release_date' : movie.release_date,
                        'running_time' : movie.running_time,
                        'actors_name'  : movie.actors.first_name
                    }    
                )
            return JsonResponse({'result':result}, status = 200)    
        except KeyError:
            return JsonResponse({'result':'key_error'}, status = 400)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            Movie.objects.create(
                title = data['title'],
                release_date = data['release_date'],
                running_time = data['running_time'],
                
            )
            return JsonResponse({'result':'created'}, status = 201)
        except KeyError:
            return JsonResponse({'result':'key_error'}, status = 400)
    
class ActorMovieView(View):
    def post(self, request):
        try:
            data = json.load(request.body)
            ActorMovie.objects.create(
                #_id를 써야하나..?
                actor_id = data['actor_name'].id,
                movie_id = data['movie_name'].id
            )
            return JsonResponse({'result':'created'}, status = 201)
        except KeyError:
            return JsonResponse({'result':'key_error'}, status = 400)
            


# http -v POST http://127.0.0.1:8000/movie/actor 'first_name'='ej' 'last_name'='k' 'date_of_birth'='93-02-02'
# http -v GET http://127.0.0.1:8000/movie/actor
