from django.db import models

# Create your models here.

class Colaborator(models.Model):
    image=models.ImageField(verbose_name="Imagen", upload_to="colaborators")
    name=models.CharField(max_length=200, verbose_name="Nombre")
    description=models.TextField(verbose_name="Cargo")   
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name="profesional"
        verbose_name_plural="profesionales"
        ordering=['name']
    
    def __str__(self):
        return self.name

