from django.urls import path

from movie.views import ActorView, MovieView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('', MovieView.as_view())
]