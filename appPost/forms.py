from django import forms
from models import Post
class PostForm(forms.Form):
     class Meta:
         model = Post
         fields = '__all__'

#class ClienteFormulario(forms.Form):
#     # Campos del Formulario
#     celular = forms.CharField(max_length=15)
#     nombre = forms.CharField(max_length=40)
#     apellido = forms.CharField(max_length=40)
#     direccion = forms.CharField(max_length=40)
#     email = forms.EmailField()
#     localidad = forms.CharField(max_length=40)



# Creo mi propio formulario para registro de usuarios a partir de la clase formulario 
# UserCreationForm

# class  UsuarioRegistroForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
#     password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)  

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1','password2']
#         #Sacar los mensajes de ayuda
#         help_texts = {k:"" for k in fields}

# class  UsuarioEditForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(label="Nombre")
#     last_name = forms.CharField(label="Apellido")
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
#     password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)  

#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email', 'password1','password2']
#         #Sacar los mensajes de ayuda
#         help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()
