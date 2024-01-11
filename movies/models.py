from django.db import models

from actors.models import Actor
from genres.models import Genre


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500, unique=True)
    release_date = models.DateField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title
