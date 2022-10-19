
from django.db import models
import uuid

from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Pelicula(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=500)
    image=models.ImageField(upload_to='photos', null=False, blank=False)
    slug=models.SlugField(unique=True, blank=False, null=False)
    sipnosis=models.TextField(max_length=300)
    autor_res=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.nombre and not instance.slug:
        slug = slugify(instance.nombre)

        while Pelicula.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8] )
            )

        instance.slug = slug


pre_save.connect(set_slug, sender=Pelicula)