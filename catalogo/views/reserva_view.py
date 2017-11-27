from ..models.reserva import Reserva
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class ReservaSerializer(serializers.ModelSerializer):
    
    cliente_nombre = serializers.SerializerMethodField()
    empleado_trabajador = serializers.SerializerMethodField()
    oficina_nro_oficina = serializers.SerializerMethodField()

     
    class Meta:
        model = Reserva
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_cliente_nombre(self, obj):
         return "%s " % (obj.cliente.nombre)

    def get_empleado_trabajador(self, obj):
         return "%s " % (obj.empleado.trabajador)

    def get_oficina_nro_oficina(self, obj):
         return "%s " % (obj.oficina.nro_oficina)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
   