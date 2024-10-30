from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json


def genre_list(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)


@csrf_exempt
def genre_create(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


@csrf_exempt
def genre_detail(request, pk):
    if request.method == "GET":
        genre = get_object_or_404(Genre, pk=pk)
        return JsonResponse({"id": genre.id, "name": genre.name})
