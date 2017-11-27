from ..models.detalleAlquiler import DetalleAlquiler
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class DetalleAlquilerSerializer(serializers.ModelSerializer):
    
    alquiler_fecha = serializers.SerializerMethodField()
    descripcion_nro_oficina = serializers.SerializerMethodField()

     
    class Meta:
        model = DetalleAlquiler
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_alquiler_fecha(self, obj):
         return "%s " % (obj.alquiler.fecha)

    def get_descripcion_nro_oficina(self, obj):
         return "%s " % (obj.descripcion.nro_oficina)


class DetalleAlquilerViewSet(viewsets.ModelViewSet):
    queryset = DetalleAlquiler.objects.all()
    serializer_class = DetalleAlquilerSerializer
 