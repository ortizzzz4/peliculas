from django.urls import path


app_name='peliculas'

from . import views

urlpatterns = [
    path('buscar' , views.ProductSearchListView.as_view(), name='buscar'),
    path('<slug:slug>' , views.PeliculaDetailView.as_view(), name='pelicula'),
]
