from django.db import models
from core.models import User, Persona

# Create your models here.

class Cliente(models.Model):

    ruc = models.CharField(max_length=10, blank=True)
    cliente = models.OneToOneField(Persona)
    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.cliente)
