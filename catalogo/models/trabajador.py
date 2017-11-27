from django.db import models
from core.models import User, Persona
from .tipoTrabajador import TipoTrabajador

# Create your models here.


class Trabajador(models.Model):

    tipoEmpleado = models.ForeignKey(TipoTrabajador)
    trabajador = models.OneToOneField(User)
    

    
    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return '%s ' % (self.trabajador)

