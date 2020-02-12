from django.db import models

class Articulo(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    precio = models.DecimalField('Precio Unitario', max_digits=5, decimal_places=2)
    descripcion = models.TextField('Descripción', max_length=300)

    def __str__(self):
        return self.nombre

