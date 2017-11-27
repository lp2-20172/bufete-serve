from ..models.comprobante import Comprobante
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class ComprobanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comprobante
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class ComprobanteViewSet(viewsets.ModelViewSet):
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer