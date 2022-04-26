from django import forms
#from models import Post
from django.contrib.auth.models import User 

class PosteoFormulario(forms.Form):
      # Campos del Formulario
     titulo = forms.CharField(max_length=80)
     subtitulo = forms.CharField(max_length=80)
     contenido = forms.CharField(max_length=200)
     imagen = forms.ImageField()
     #fecha_publicacion = forms.DateTimeField()
     #ultima_actualizacion = forms.DateTimeField()
     autor = forms.IntegerField()

# class PostForm(forms.Form):
#      class Meta:
#          model = Post
#          fields = ['titulo', 'subtitulo', 'contenido','imagen',
#                     'fecha_publicacion','ultima_actualizacion','autor']


