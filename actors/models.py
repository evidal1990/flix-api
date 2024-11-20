from django.db import models

NATIONALITIES = (
    ("FR", "Francês"),
    ("US", "Americano"),
    ("IT", "Italiano"),
    ("JP", "Japonês"),
    ("CH", "Chinês"),
    ("BR", "Brasileiro"),
    ("IN", "Indiano"),
    ("DE", "Alemão"),
    ("ES", "Espanhol"),
    ("GB", "Inglês"),
    ("MX", "Mexicano"),
    ("AU", "Australiano"),
    ("CA", "Canadense"),
    ("IS", "Israelense"),
)


class Actor(models.Model):

    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITIES, blank=True, null=True)

    def __str__(self):
        return self.name
