from django.urls import path
from appPost.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PostLista.as_view(), name="postLista"),
    path('post/crear/', PostCrear.as_view(), name="postCrear"),
    path('post/detalle/<pk>/', PostDetalle.as_view(), name="postDetalle"),
    path('post/editar/<pk>/', PostActualizar.as_view(), name="postActualizar"),
    path('post/eliminar/<pk>/', PostEliminar.as_view(), name="postEliminar"),
    
    path('comentario/crear/', ComentarioCrear.as_view(), name="comentarioCrear"),
    path('comentario/lista/', ComentarioLista.as_view(), name="comentariolista"),
    path('comentario/detalle/<pk>/', ComentarioDetalle.as_view(), name="comentarioDetalle"),
]