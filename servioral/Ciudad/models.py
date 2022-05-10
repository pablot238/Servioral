from email.headerregistry import Address
from django.db import models

# Create your models here.

class ciudad(models.Model):

    ciudad = models.CharField(max_length=200, null=False, verbose_name="Nombre de ciudad", choices= (
        (1, 'Armenia'),
        (2, 'Barrancabermeja'),
        (3, 'Barranquilla'),
        (4, 'Bogotá'),
        (5, 'Bucaramanga'),
        (6, 'Buga'),
        (7, 'Cali'),
        (8, 'Cartagena'),
        (9, 'Chía'),
        (10, 'Cúcuta'),
        (11, 'Duitama'),
        (12, 'Florencia'),
        (13, 'Fusagasugá'),
        (14, 'Girardot'),
        (15, 'Honda'),
        (16, 'Ibagué'),
        (17, 'Ipiales'),
        (18, 'Jamundí'),
        (19, 'Leticia'),
        (20, 'Manizales'),
        (21, 'Mariquita'),
        (22, 'Medellín'),
        (23, 'Mompox'),
        (24, 'Montería'),
        (25, 'Murillo'),
        (26, 'Neiva'),
        (27, 'Pamplona'),
        (28, 'Pasto'),
        (29, 'Pereira'),
        (30, 'Popayán'),
        (31, 'Riohacha'),
        (32, 'San Andrés y Providencia'),
        (33, 'San Antero'),
        (34, 'Santa Marta'),
        (35, 'Santafé de Antioquia'),
        (36,'Sevilla'),
        (37, 'Sincelejo'),
        (38, 'Sogamoso'),
        (39, 'Tabio'),
        (40, 'Tocancipá'),
        (41, 'Tolú'),
        (42, 'Tuluá'),
        (43, 'Tumaco')

    ))
    address = models.CharField(max_length=200, null=False, verbose_name="Dirección")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
                
    def __str__(self):
        return self.name