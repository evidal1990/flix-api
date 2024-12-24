from django.urls import path
from . import views


urlpatterns = [
    path("actors/",
         views.ActorListCreateView.as_view(), name="actor-list-create"),
    path("actors/<int:pk>/",
         views.ActorRetrieveUpdateDestroyView.as_view(), name="actor-retrieve-update-destroy"),
    path("actors/nationalities/",
         views.ActorNationalitiesView.as_view(), name="actor-nationality")
]