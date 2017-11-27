from django.db import models






class TipoTrabajador(models.Model):

    nombre = models.CharField(max_length=20)
    
    
    class Meta:
        verbose_name = "TipoTrabajador"
        verbose_name_plural = "TipoTrabajadores"

    def __str__(self):
        return '%s' % (self.nombre)

