from django.db import models

class Movie(models.Model):
    title        = models.CharField(max_length=50)
    release_date = models.DateField()
    running_time = models.IntegerField()
    
    class Meta:
        db_table = 'movies'


class Actor(models.Model):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    movie         = models.ManyToManyField("Movie", through='ActorMovie', related_name='actors')
    
    class Meta:
        db_table = 'actors'

#데이터가 자동으로 만들어지는게 아님
#단지 편하게 데이터를 꺼내올 수 있게만 해주는 것
#연결고리에 대한 생각 그만        
class ActorMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'actors_movies'
    
