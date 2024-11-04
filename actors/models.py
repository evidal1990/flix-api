from django.db import models

NATIONALITIES = (
    ("FR", "French"),
    ("US", "American"),
    ("IT", "Italian"),
    ("JP", "Japanese"),
    ("CH", "Chinese"),
    ("BR", "Brazilian"),
    ("IN", "Indian"),
    ("DE", "German"),
    ("ES", "Spanish"),
    ("GB", "British"),
    ("MX", "Mexican"),
)


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITIES, blank=True, null=True)

    def __str__(self):
        return self.name
