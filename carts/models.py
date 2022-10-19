from itertools import product
import uuid
from django.db import models
from users.models import User
from peliculas.models import Pelicula

from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Pelicula, through='CartProducts')
    
    created_at = models.DateTimeField(auto_now_add=True)

   # FEE = 0.05 # 0.5%

    def __str__(self):
        return self.cart_id
    
    
    def products_related(self):
        return self.cartproducts_set.select_related('product')

    def has_products(self):
        return self.products.exists()
    
class CartProductsManager(models.Manager): #manejador de objetos crear o atualizar
    def create_or_update_quantity(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)
        
        if not created:
              quantity = object.quantity + quantity
            
              
        object.update_quantity(quantity)
        return object
         
class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CartProductsManager()
    
    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()   
    
    
def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())
    
#def update_totals(sender, instance, action, *args, **kwargs):
 #   if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
  #     instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()

        
        
pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartProducts)
#m2m_changed.connect(update_totals, sender=Cart.products.through)
