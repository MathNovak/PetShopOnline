from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField, ValidationError
from typing import List
'''from rest_framework.authtoken import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet'''
from rest_framework import generics
#from termios import CDSUSP

from reserva.models import Reserva, Petshop, Animal

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only = True,
        view_name = 'api:reserva-detail'
    )
    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__' 




class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )
    class Meta:
        model = Reserva
        fields = '__all__'




class AnimalSerializer(ModelSerializer):
    animal = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'api:reserva-detail'
    )
    class Meta:
        model = Animal
        fields = 'all'

class AnimalPorCategoria(generics.ListAPIView):
    serializer_class = AnimalSerializer
