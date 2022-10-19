from django.db import models

# Create your models here.

from django.db import models

from peliculas.models import Pelicula

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    pelicula = models.ManyToManyField(Pelicula, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title