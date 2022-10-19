"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from peliculas.views import PeliculaListView
#from serie.views import SerieListView
from . import views


urlpatterns = [
    path('inicio/', PeliculaListView.as_view(), name='index'),
    path('usuarios/logout', views.logout_view , name='logout' ),
    path('', views.login_view , name='login' ),
    path('usuarios/register', views.register , name='register' ),


    path('admin/', admin.site.urls),
    
    path('peliculas/',include('peliculas.urls')),
    path('favorite/', include('carts.urls')),
    #path('serie/',include('serie.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
