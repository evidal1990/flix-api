from django.contrib import admin
from django.urls import path
from genres.views import GenreListView, GenreUpdateView, GenreDeleteView, GenreCreateView, GenreDetailView, GenreListView
from actors.views import ActorListView, ActorUpdateView, ActorDeleteView, ActorCreateView, ActorDetailView, ActorListView
from movies.views import MovieListView, MovieUpdateView, MovieDeleteView, MovieCreateView, MovieDetailView, MovieListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/create", GenreCreateView.as_view(), name="genre-create"),
    path("genres/update/<int:pk>", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/delete/<int:pk>", GenreDeleteView.as_view(), name="genre-delete"),
    path("genres/detail/<int:pk>", GenreDetailView.as_view, name="genre-detail"),
    path("genres/list", GenreListView.as_view(), name="genre-list"),

    path("actors/create", ActorCreateView.as_view(), name="actor-create"),
    path("actors/update/<int:pk>", ActorUpdateView.as_view(), name="actor-update"),
    path("actors/delete/<int:pk>", ActorDeleteView.as_view(), name="actor-delete"),
    path("actors/detail/<int:pk>", ActorDetailView.as_view(), name="actor-detail"),
    path("actors/list", ActorListView.as_view(), name="actor-list"),

    path("movies/create", MovieCreateView.as_view(), name="actor-create"),
    path("movies/update/<int:pk>", MovieUpdateView.as_view(), name="actor-update"),
    path("movies/delete/<int:pk>", MovieDeleteView.as_view(), name="actor-delete"),
    path("movies/detail/<int:pk>", MovieDetailView.as_view(), name="actor-detail"),
    path("movies/list", MovieListView.as_view(), name="actor-list"),
]
