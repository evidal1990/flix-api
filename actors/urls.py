from django.urls import path
from . import views


urlpatterns = [
    path("actors/create",
         views.ActorCreateView.as_view(), name="actor-create"),
    path("actors/update/<int:pk>",
         views.ActorUpdateView.as_view(), name="actor-update"),
    path("actors/delete/<int:pk>",
         views.ActorDeleteView.as_view(), name="actor-delete"),
    path("actors/detail/<int:pk>",
         views.ActorDetailView.as_view(), name="actor-detail"),
    path("actors/list", views.ActorListView.as_view(), name="actor-list"),
]
