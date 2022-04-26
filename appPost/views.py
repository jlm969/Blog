from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from appPost.models import *
from appPost.forms import PosteoFormulario
from appUsuario.models import Avatar
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

 
def posteo(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None

    posteos = Post.objects.all()
    if request.method == 'POST':
         posteo = PosteoFormulario(request.POST)
         if posteo.is_valid():    
            datos = posteo.cleaned_data
            print(datos)
            posteo_nuevo = Post(datos['titulo'], datos['subtitulo'], datos['contenido'], datos['imagen'],datos['autor'])        
            posteo_nuevo.save()       
            formulario = PosteoFormulario()
            return render(request, "appPost/posteo.html",{"posteos":posteos, "title":"Post", "page":"Posteos","formulario":formulario, "imagen_url": imagen})
         else: 
             formulario = PosteoFormulario()
             return render(request, "appPost/posteo.html",{"posteos":posteos, "title":"Post", "page":"Error en datos","formulario":formulario, "imagen_url": imagen})   
    else:
         formulario = PosteoFormulario()
         return render(request, "appPost/posteo.html",{"posteos":posteos, "title":"Post", "page":"Posteos","formulario":formulario, "imagen_url": imagen})


    

class PostLista(ListView):    
    model = Post
    template_name = "appPost/postLista.html" 

# CreateView -- Crear un item  
class PostCrear(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['titulo','subtitulo','contenido','imagen', 'autor']
    success_url = "/posteo"
  
# UpdateView -- Actualizar  un item
class PostActualizar(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['titulo','subtitulo','contenido','imagen','autor']
    success_url = "/posteo"
 

# DetailView -- obtengo un solo item
class PostDetalle(DetailView):
    model = Post
    template_name = "appPost/postDetalle.html" 


# DeleteView -- Borrar un item
class PostEliminar(DeleteView):
    model = Post
    success_url = "/" 


# CreateView -- Crear un Comentario 
class ComentarioCrear(LoginRequiredMixin,CreateView):
    model = Comentario
    fields = ['post','contenido','autor']
    success_url = "/"

class ComentarioLista(ListView):
    model = Comentario
    template_name = "appPost/comentarioLista.html" 


class ComentarioDetalle(LoginRequiredMixin,DetailView):
    model = Comentario
    template_name = "appPost/comentarioDetalle.html" 