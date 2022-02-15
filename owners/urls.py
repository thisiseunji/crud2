from django.urls import path

from owners.views import OwnerAndDogsView, OwnersView, DogsView

urlpatterns = [
    path('', OwnersView.as_view()),
    path('/dogs', DogsView.as_view()),
    path('/oads', OwnerAndDogsView.as_view())
]
