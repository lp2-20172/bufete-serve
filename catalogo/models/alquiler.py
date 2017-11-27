from django.db import models
from .cliente import Cliente
from .trabajador import Trabajador
from .comprobante import Comprobante

# Create your models here.



class Alquiler(models.Model):

    
    
    fecha = models.DateField(null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    nroDoc = models.CharField(max_length=8)
    trabajador = models.ForeignKey(Trabajador)
    comprobante = models.ForeignKey(Comprobante)
    total = models.FloatField(default=0)
    direccion = models.CharField(max_length=100)
    nroBoleta = models.FloatField(default=0)
    
    
       

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return '%s' % (self.fecha)