from django.urls import path
from appUsuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('about', about, name="about"),
    path('', inicio, name="Inicio"),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='Register'),
    path('logout/', LogoutView.as_view(template_name="appUsuario/logout.html"), name='logout'),
    path('editar/', actualizar_usuario, name='edit'),
    path("cargar_imagen/", cargar_imagen, name="CargarImagen"),
    path('mensaje/lista/', MensajeLista.as_view(), name="mensajeLista"),
    path('mensaje/enviar/', MensajeEnviar.as_view(), name="mensajeEnviar"),
    path('mensaje/leer/<pk>/', MensajeLeer.as_view(), name="mensajeLeer"),
]