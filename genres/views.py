from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializers


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreUpdateView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreDeleteView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
