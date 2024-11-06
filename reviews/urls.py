from django.urls import path
from . import views


urlpatterns = [
    path("reviews/create", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews/update/<int:pk>",
         views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/delete/<int:pk>",
         views.ReviewDeleteView.as_view(), name="review-delete"),
    path("reviews/detail/<int:pk>",
         views.ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/list", views.ReviewListView.as_view(), name="review-list"),
]
