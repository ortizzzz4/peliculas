from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from carts.models import Cart, CartProductsManager
from .utils import get_or_create_cart
# Create your views here.
from peliculas.models import Pelicula

def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
       'cart': cart
    })

def add(request,product_id):
   # cart=get_or_create_cart(request)
   # product=get_object_or_404(Pelicula, pk=request.POST.get('product_id'))
   # product = Pelicula.objects.all(pk=product_id)
   # product.save()
   
    cart = get_or_create_cart(request)
    product = get_object_or_404(Pelicula, pk=request.POST.get('product_id'))

   # cart.products.add(product)
    
   
    cart.products.add(product)
    quantity = int(request.POST.get('quantity', 1))
   
   
   # cart_product = CartProductsManager.objects.create_or_update_quantity(cart=cart,
   #                                                                    product=product,
    #                                                                   quantity=quantity)
  
    return render(request, 'carts/add.html', {
       'quantity': quantity,
       # 'cart_product': cart_product,
        ' product':product,
        
    })
   



def remove(request,product_id):
     cart = get_or_create_cart(request)
     product = get_object_or_404(Pelicula, pk=request.POST.get('product_id'))

     cart.products.remove(product)

     return redirect('carts:cart')
#def remove(request, id):
 #   cart=get_or_create_cart(request)
  #  product= Pelicula.objects.get(pk=id)
   # if request.method == 'POST':
    #    cart.products.remove(product)
     #   #product.delete()
      #  return redirect('carts:cart')
    #context = {'object': product}
    #return render(request, 'remove.html', context)