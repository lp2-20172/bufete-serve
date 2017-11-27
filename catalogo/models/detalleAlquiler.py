from django.db import models
from .alquiler import Alquiler
from .oficina import Oficina
# Create your models here.

class DetalleAlquiler(models.Model):

    precio = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)
    fecha = models.DateField(auto_now_add=True)
    alquiler = models.ForeignKey(Alquiler)
    descripcion = models.OneToOneField(Oficina)   
    importe = models.FloatField(default=0)

    class Meta:
        verbose_name = "DetalleAlquiler"
        verbose_name_plural = "DetalleAlquileres"

    def __str__(self):
        return '%s' % (self.alquiler)
