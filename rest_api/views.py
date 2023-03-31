import json
from reserva.models import Reserva
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_api.serializers import AgendamentoModelSerializer, PetshopNestedModelSerializer

from reserva.models import Reserva, Petshop


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopNestedModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticatedOrReadOnly]

@api_view()
def reservas(request):
    consulta = Reserva.objects.all()
    dados = []
    for reserva in consulta:
        dado = {
            'id': reserva.id,
            'nome': reserva.nome,
            'telefone': reserva.telefone,
        }
        dados.append(dado)
    return Response(dados)

@api_view(http_method_names=['POST'])
def adicionar_reserva(request):
    nome = request.POST['nome']
    reserva = Reserva.objects.create(nome=nome, telefone=telefone)
    dado = {
        'id': reserva.id,
        'nome': reserva.nome,
        'telefone': reserva.telefone
    }
    return Response(dado)