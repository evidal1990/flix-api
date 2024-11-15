from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializers


class MovieListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
