from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
import json


def list(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)


@csrf_exempt
def create(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


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
