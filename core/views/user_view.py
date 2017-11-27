from ..models import User
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce



class UserSerializer(serializers.ModelSerializer):

	

     
    class Meta:
        model = User
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    


         


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
