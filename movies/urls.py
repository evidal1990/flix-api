from django.urls import path
from . import views


urlpatterns = [
    path("movies/create", views.MovieCreateView.as_view(), name="actor-create"),
    path("movies/update/<int:pk>",
         views.MovieUpdateView.as_view(), name="actor-update"),
    path("movies/delete/<int:pk>",
         views.MovieDeleteView.as_view(), name="actor-delete"),
    path("movies/detail/<int:pk>",
         views.MovieDetailView.as_view(), name="actor-detail"),
    path("movies/list", views.MovieListView.as_view(), name="actor-list"),
]
