from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return (f"{self.user} | {self.imagen}")

class Mensaje(models.Model):

    destinatario = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=80)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.destinatario} | {self.asunto} | {self.cuerpo} | {self.fecha}")