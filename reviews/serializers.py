from rest_framework import serializers
from django.db.models import Avg
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def get_movies_average_stars():
        stars_average = Review.objects.aggregate(
            stars_avg=Avg("stars"))["stars_avg"]
        return round(stars_average, 1) if stars_average else 0
