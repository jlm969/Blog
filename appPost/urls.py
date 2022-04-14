from django.urls import path
from appPost.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', inicio, name="Inicio"),
    path('', PostLista.as_view(), name="postLista"),
  # A la url
    #path('post/lista/', PostLista.as_view(), name="postLista"),
    path('post/nuevo/', PostCrear.as_view(), name="postCrear"),
    path('post/detalle/<pk>/', PostDetalle.as_view(), name="postDetalle"),
    path('post/editar/<pk>/', PostActualizar.as_view(), name="postActualizar"),
    path('post/eliminar/<pk>/', PostEliminar.as_view(), name="postEliminar"),
]