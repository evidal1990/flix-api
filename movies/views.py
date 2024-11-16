from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from movies.models import Movie
from movies.serializers import MovieSerializers
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        movies_total = self.queryset.count()
        movies_by_genre = self.queryset.values(
            "genre__name").annotate(count=Count("id"))
        movies_by_actor = self.queryset.values(
            "actors__name").annotate(count=Count("id"))
        movies_reviews = Review.objects.count()
        movies_average_stars = Review.objects.aggregate(
            stars_avg=Avg("stars"))["stars_avg"]

        return response.Response(
            data={
                "movies_total": movies_total,
                "movies_by_genre": movies_by_genre,
                "movies_by_actor": movies_by_actor,
                "movies_reviews": movies_reviews,
                "movies_average_stars": round(movies_average_stars, 1) if movies_average_stars else 0,
            }, status=status.HTTP_200_OK)
