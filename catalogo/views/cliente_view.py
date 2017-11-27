from ..models.cliente import Cliente
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class ClienteSerializer(serializers.ModelSerializer):
    
    cliente_nombre = serializers.SerializerMethodField()

     
    class Meta:
        model = Cliente
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_cliente_nombre(self, obj):
         return "%s " % (obj.cliente.nombre)

    


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer