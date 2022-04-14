from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


# Creo mi propio formulario para registro de usuarios a partir de la clase formulario 
# UserCreationForm

#class  Usuario(User):
#   pass

#   def __str__(self):
#         return self.user_name
    # email = forms.EmailField()
    # password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    # password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)  

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1','password2']
    #     #Sacar los mensajes de ayuda
    #     help_texts = {k:"" for k in fields}



class Post(models.Model):

    titulo = models.CharField(max_length=80)
    contenido = models.TextField()
    imagen = models.ImageField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
   # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo

class Comentario(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

 #   def __str__(self):
 #       return self.usuario.username

class VistaPost(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_vista = models.DateTimeField(auto_now_add=True)

#  def __str__(self):
#     return self.usuario.username  

class MeGusta(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

  #  def __str__(self):
  #      return self.usuario.user_name  