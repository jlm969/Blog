
from dataclasses import field
from re import template
from winreg import DeleteValue
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from appUsuario.models import *
 #importamos la clase Form de django
from appUsuario.forms import AvatarFormulario, UsuarioRegistroForm, UsuarioEditForm


# Autenticacion Django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout , authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Vistas Basadas en Clases 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 

# Create your views here.

def about(request):
    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None
    dict_ctx = {"title": "Inicio", "page": "","imagen_url": imagen}
    return render(request, "appUsuario/about.html", dict_ctx)

def inicio(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None
    dict_ctx = {"title": "Inicio", "page": "","imagen_url": imagen}
    return render(request, "appUsuario/index.html", dict_ctx)
 



def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre_usuario = data.get("username")
            contra = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contra)

            if usuario is not None:
                login(request, usuario)
                #dict_ctx = {"title": "Inicio", "mensaje": "Bienvenido!!!", "page": usuario}
                #return render (request, "appPost/postLista.html", dict_ctx)
                return redirect ("posteo")
            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors":["El usuario no existe"]}
                return render (request, "appUsuario/index.html", dict_ctx)
               
        else:
            dict_ctx = {"title": "Inicio", "page": "Usuario Anonimo", "errors":["Revise datos enviados en el formulario"]}
            return render (request, "appUsuario/index.html", dict_ctx)
            
    else:
        form = AuthenticationForm()
        return render (request,"appUsuario/login.html", {"form": form})

def register_request(request):
     if request.method == "POST":
        # Formulario Propio de Registro
         form = UsuarioRegistroForm(request.POST)
         if form.is_valid():
             usuario = form.cleaned_data.get("username")
             form.save()
             dict_ctx = {"title": "Register", "page": "Usuario Registrado"}
             return render (request, "appUsuario/index.html", dict_ctx)
               
         else:
             dict_ctx = {"title": "Inicio", "page": "Datos Invalidos", "errors":["No paso las validaciones"]}
             return render (request, "appUsuario/index.html", dict_ctx) 
            
            
     else:
         # Formulario Propio de Registro
        form = UsuarioRegistroForm()
        return render (request,"appUsuario/register.html", {"form": form} )

@login_required()
def actualizar_usuario(request):
     usuario = request.user
     if request.method == "POST":
         form = UsuarioEditForm(request.POST)  #contiene los valores que vienen de la peticion
         if form.is_valid():
             data = form.cleaned_data
             usuario.email = data["email"]
             usuario.first_name = data["first_name"]
             usuario.last_name = data["last_name"]
             usuario.descripcion = data["descripcion"]
             usuario.webpage = data["webpage"]
             usuario.password1 = data["password1"]
             usuario.password2 = data["password2"]
             usuario.save()
             return redirect ("posteo")
         else:
             #form = UsuarioEditForm(initial={'email':usuario.email , 'first_name':usuario.first_name,'last_name':usuario.last_name})
             #erros = {"errors":["No paso las validaciones"]}
             #return render(request, "apppedido/editar_usuario.html", {"form":form}, erros )
             form = UsuarioEditForm(initial={"email": usuario.email})  
             return render(request,  "appUsuario/editar_usuario.html", {"form": form, "errors": ["Datos invalidos"]})

     else:
         form = UsuarioEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name,'last_name':usuario.last_name})
         return render(request, "appUsuario/editar_usuario.html", {"form":form})

@login_required()
def cargar_imagen(request):
    if request.method == "POST":
       formulario = AvatarFormulario(request.POST,request.FILES)
       if formulario.is_valid():
           usuario = request.user
           avatar = Avatar.objects.filter(user=usuario)
           if len(avatar) > 0:
               avatar = avatar[0]
               avatar.imagen = formulario.cleaned_data["imagen"]
               avatar.save()
           else:
               avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
               avatar.save()      
           return redirect("Inicio")
           
    else:
        formulario = AvatarFormulario()
        return render(request, "appUsuario/cargarImagen.html", {"form": formulario})


# CreateView -- Crear un Comentario 
class MensajeEnviar(CreateView):
    model = Mensaje
    fields = ['destinatario','asunto','cuerpo']
    success_url = "/appUsuario"

class MensajeLista(ListView):
    model = Mensaje
    template_name = "appUsuario/mensajeLista.html" 


class MensajeLeer(DetailView):
    model = Mensaje
    template_name = "appUsuario/mensajeLeer.html" 