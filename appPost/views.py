from django.shortcuts import render

# Vistas Basadas en Clases 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView


# Autenticacion Django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout , authenticate

# Mixin y Decoradores Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from appPost.models import Post, Comentario, VistaPost, MeGusta


# Create your views here.

# Create your views here.

def inicio(request):

 #   if request.user.username:
 #       avatar = Avatar.objects.filter(user=request.user)

 #       if len(avatar) > 0:
 #           imagen = avatar[0].imagen.url
  #      else:
  #          imagen = None
  #  else:
  #      imagen = None
    #dict_ctx = {"title": "Inicio", "page": "BLOG","imagen_url": imagen}
    dict_ctx = {"title": "Inicio", "page": "BLOG"}
  #  return render(request, "apppedido/index.html", dict_ctx)
    return render(request, "appPost/index.html", dict_ctx)




# Vistas Basadas en Clases 

# ListView -- Listar contenido
# A este tipo de Vistas basadas en  Clases  le puedo pasar  LoginRequiredMixin  
# para que solo un usuario logueado pueda accederla
# y va al principio!!!  

#class PostLista(LoginRequiredMixin, ListView):
class PostLista(ListView):
    model = Post
    template_name = "appPost/postLista.html" 

# CreateView -- Crear un item  
class PostCrear(CreateView):
    model = Post
   # success_url = "/appPost/lista"
    template_name = "appPost/postCrear.html" 
    fields = ['titulo','contenido' ]
    
    

# UpdateView -- Actualizar  un item
class PostActualizar(UpdateView):
    model = Post
    fields = ['titulo','contenido','imagen' ]
    # success_url = "/appPost/lista"
    #template_name = "appPost/postActualizar.html" 


# DetailView -- obtengo un solo item
class PostDetalle(DetailView):
    model = Post
    template_name = "appPost/postDetalle.html" 


# DeleteView -- Borrar un item
class PostEliminar(DeleteView):
    model = Post
    success_url = "post/lista" 

