from django.db import models
from tabnanny import verbose 
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    image=models.ImageField(verbose_name="Imagen",upload_to="blog")
    title=models.CharField(max_length=200,verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    
    def __str__(self):
        return self.title