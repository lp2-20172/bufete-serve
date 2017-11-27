from django.db import models

# Create your models here.

class Comprobante(models.Model):

    descripcion = models.CharField(max_length=10, blank=True)
    

    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"

    def __str__(self):
        return '%s' % (self.descripcion)
