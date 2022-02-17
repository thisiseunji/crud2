from django.urls import path, include

urlpatterns = [
    path('owners', include('owners.urls')),
    path('movie', include('movie.urls')),
]