from ..models.alquiler import Alquiler
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class AlquilerSerializer(serializers.ModelSerializer):
    
    comprobante_descripcion = serializers.SerializerMethodField()
    trabajador_username = serializers.SerializerMethodField()

     
    class Meta:
        model = Alquiler
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_comprobante_descripcion(self, obj):
         return "%s " % (obj.comprobante.descripcion)

    def get_trabajador_username(self, obj):
         return "%s " % (obj.trabajador.username)


class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer

    