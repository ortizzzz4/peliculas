from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
#"from users.models import User



from django.contrib import messages

from peliculas.models import Pelicula

#from serie.models import Serie

from .form import RegisterForm
#from productos.models import Producto

def index(request):
    
    pelicula =Pelicula.objects.all().order_by('-id')
    #serie=Serie.objects.all().order_by('-id')
    
    return render(request, 'index.html',{

         
         'pelicula':pelicula,
      #   'serie':serie
          
    })
    
def login_view(request):
        if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              
              user=authenticate(username=username, password=password)
              if user:
                    login(request,user)
                    messages.success(request,'¡Welcome {}'.format(user.username))
                    return redirect('index')
              else:
                    messages.error(request,'Username or password incorrect')#mensaje de error
    
        return render(request, 'users/login.html',{
        
    })
        
        
def logout_view(request):
      
    logout(request)
    messages.success(request, 'successfully logged out')#mensaje de salida
    return redirect('login')
def register(request):
    form  = RegisterForm(request.POST or None)
    
    if request.method=='POST' and form.is_valid():
         user =  form.save()
         if user: 
              login(request, user)
              messages.success(request, 'User created successfully')#Mensaje de usuario creado
              return redirect('index')
    
      
    return render(request, 'users/register.html',{
        'form': form
       
    })