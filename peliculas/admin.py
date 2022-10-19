from django.contrib import admin

from peliculas.models import Pelicula

# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
      fields = ('nombre','descripcion','image','sipnosis','autor_res')
      list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Pelicula,PeliculaAdmin)