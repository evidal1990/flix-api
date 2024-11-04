from genres.models import Genre
from genres.serializers import GenreSerializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
import json


class ListCreateView(generics.ListCreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializers


@csrf_exempt
def detail(request, pk):
    if request.method == "GET":
        genre = get_object_or_404(Genre, pk=pk)
        return JsonResponse({"id": genre.id, "name": genre.name}, status=200)


@csrf_exempt
def update(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        genre = get_object_or_404(Genre, pk=pk)
        genre.name = data["name"]
        genre.save()
        return JsonResponse({"id": genre.id, "name": genre.name}, status=200)


@csrf_exempt
def delete(request, pk):
    if request.method == "DELETE":
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return JsonResponse({"message": "Gênero excluído com sucesso"}, status=204)
