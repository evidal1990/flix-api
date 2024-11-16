from django.urls import path
from . import views


urlpatterns = [
    path("genres/create",
         views.GenreCreateView.as_view(), name="genre-create"),
    path("genres/update/<int:pk>",
         views.GenreUpdateView.as_view(), name="genre-update"),
    path("genres/delete/<int:pk>",
         views.GenreDeleteView.as_view(), name="genre-delete"),
    path("genres/detail/<int:pk>",
         views.GenreDetailView.as_view, name="genre-detail"),
    path("genres/list", views.GenreListView.as_view(), name="genre-list"),
]
