from ..models.trabajador import Trabajador
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class TrabajadorSerializer(serializers.ModelSerializer):
    
    tipoEmpleado_tipoEmpleado = serializers.SerializerMethodField()
    trabajador_username = serializers.SerializerMethodField()

     
    class Meta:
        model = Trabajador
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_tipoEmpleado_tipoEmpleado(self, obj):
         return "%s " % (obj.tipoEmpleado.nombre)

    def get_trabajador_username(self, obj):
         return "%s " % (obj.trabajador.username)


class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
