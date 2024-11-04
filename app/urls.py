"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateView, GenreUpdateView, GenreDeleteView, GenreDetailView, GenreListView
from actors.views import ActorListView, ActorCreateView, ActorDetailView, ActorUpdateView, ActorDeleteView


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
]
