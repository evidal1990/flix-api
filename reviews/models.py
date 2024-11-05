from django.db import models
from django.core.validators import MinValueValidator as MinVal, MaxValueValidator as MaxVal
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinVal(1, "A avaliação não pode ser inferior a 1 estrelas"),
            MaxVal(5, "A avaliação não pode ser superior a 5 estrelas")
        ])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
