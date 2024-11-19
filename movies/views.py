from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializers, MovieStatsSerializer
from reviews.serializers import ReviewSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieStatsView(views.APIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        data = {
            "movies_total": self.queryset.count(),
            "movies_by_genre": MovieStatsSerializer.get_movies_by_genre(),
            "movies_by_actor": MovieStatsSerializer.get_movies_by_actor(),
            "movies_reviews": Review.objects.count(),
            "movies_avg_stars": ReviewSerializer.get_movies_average_stars(),
        }
        return response.Response(data=data, status=status.HTTP_200_OK)
