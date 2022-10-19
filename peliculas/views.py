from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Q

from .models import Pelicula

class PeliculaListView(ListView):
    template_name='index.html'
    queryset=Pelicula.objects.all().order_by('-id')
   # paginate_by=2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] ='Welcome'
        
        
        
        return context
    
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'pelicula.html'
    
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
         
        return context
    
class ProductSearchListView(ListView):
            template_name = 'snippets/buscar.html'
            def get_queryset(self):
                  filters = Q(nombre__icontains=self.query()) | Q(category__title__icontains=self.query())
                  return Pelicula.objects.filter(filters)
           
            def query(self):
                return self.request.GET.get('q')
      
            def get_context_data(self, **kwargs):
                   context = super().get_context_data(**kwargs)
                   context['query'] = self.query()
                   #context['count'] = context['product_list'].count()

                   return context
       
   
    
    