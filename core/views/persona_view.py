from ..models import Persona
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce



class PersonaSerializer(serializers.ModelSerializer):

	

     
    class Meta:
        model = Persona
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    


         


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
