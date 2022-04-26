from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):

    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posteos', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
         return f"{self.titulo} | {self.imagen} | {self.autor}"

class Comentario(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.post.titulo} | {self.contenido}  | {self.fecha_comentario }  | {self.autor}"
       

class VistaPost(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_vista = models.DateTimeField(auto_now_add=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Post:{self.post.titulo}  |  Visto:  {self.usuario}  | Fecha: {self.fecha_vista}"

class MeGusta(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
       return f"Post:{ self.post.titulo }  | Me Gusta: {self.usuario}"