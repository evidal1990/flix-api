from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializers


class ListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class CreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class DetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class UpdateView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class DeleteView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
