from django.db import models
from .categoria import Categoria



class Oficina(models.Model):
    
    codigo = models.CharField(max_length=10,null=True, blank=True)
    nro_oficina = models.CharField(max_length=10,null=True, blank=True)
    estado = models.BooleanField(default=False)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.FloatField(default=0)
    categoria = models.ForeignKey(Categoria)
        

    class Meta:
        verbose_name = "Oficina"
        verbose_name_plural = "Oficinas"

    def __str__(self):
        return '%s' % (self.codigo)