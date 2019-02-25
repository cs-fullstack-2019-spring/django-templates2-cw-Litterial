from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('movies/',views.moviesFunc, name='movies'),
    path('movies/details/<int:movie_id>',views.movieDetails,name='details'),
    path('movies/synopsis/<int:movie_id>',views.movieSynopsis,name='synopsis'),

]