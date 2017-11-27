from django.contrib import admin
from catalogo.models.oficina import Oficina
from catalogo.models.alquiler import Alquiler
from catalogo.models.categoria import Categoria
from catalogo.models.cliente import Cliente
from catalogo.models.trabajador import Trabajador
from catalogo.models.tipoTrabajador import TipoTrabajador
from catalogo.models.detalleAlquiler import DetalleAlquiler
from catalogo.models.comprobante import Comprobante
from catalogo.models.reserva import Reserva




# Register your models here.


admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Oficina)
admin.site.register(Trabajador)
admin.site.register(TipoTrabajador)
admin.site.register(Alquiler)
admin.site.register(DetalleAlquiler)
admin.site.register(Comprobante)

admin.site.register(Reserva)


