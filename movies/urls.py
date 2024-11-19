from django.urls import path
from . import views


urlpatterns = [
    path("movies/",
         views.MovieListCreateView.as_view(), name="actor-list-create"),
    path("movies/<int:pk>/",
         views.MovieRetrieveUpdateDestroyView.as_view(), name="actor-retrieve-update-destroy"),
    path("movies/stats/",
         views.MovieStatsView.as_view(), name="movie-stats")
]
