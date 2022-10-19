from django.urls import path
from . import views
#from . import EliminarCarrito
app_name = 'carts'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('añadir/<int:product_id>', views.add, name='add'),
    path('eliminar/<int:product_id>' ,views.remove, name='remove'),
   # path('EliminarCarrito/<int:pk>', views.EliminarCarrito.as_view(),name='EliminarCarrito' ),
    
]