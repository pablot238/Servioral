from django.db import models

# Create your models here.

class servicio(models.Model):

    id_servicio =  models.AutoField(primary_key=True, verbose_name="Id paciente")
    title = models.CharField(max_length=200, null=False, verbose_name="Titulo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
                
    def __str__(self):
        return self.title