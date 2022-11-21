from django.db import models


# Create your models here.

class Service(models.Model):
    image=models.ImageField(verbose_name="Imagen", upload_to="services")
    title=models.CharField(max_length=200, verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=['-created']
    
    def __str__(self):
        return self.title


