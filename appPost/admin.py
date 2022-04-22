from django.contrib import admin
from appPost.models import Post, Comentario, VistaPost, MeGusta
# Register your models here.

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(VistaPost)
admin.site.register(MeGusta)
