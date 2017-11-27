from ..models.oficina import Oficina
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class OficinaSerializer(serializers.ModelSerializer):
    
    categoria_nombre = serializers.SerializerMethodField()

     
    class Meta:
        model = Oficina
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_categoria_nombre(self, obj):
         return "%s " % (obj.categoria.nombre)
        
    
    


class OficinaViewSet(viewsets.ModelViewSet):
    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(estado__icontains=query),
                    Q(descripcion__icontains=query),
                    Q(precio__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset

    