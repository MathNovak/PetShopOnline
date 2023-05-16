import pytest
import datetime
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
#from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'brian', 'email': 'brian@email.com', 'nome_pet': 'kawan ',
        'data' : hoje, 'turno': 'manhã', 'tamanho': 0, 'observacao': '', 'petshop': petshop.pk,
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_resgate_agendamento(dados_agendamento):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.get('/api/agendamento', dados_agendamento)
    assert response.status_code == 200

@pytest.mark.django_db
def test_att_agendamento():     #att - atualizacao
    att = Reserva.objects.filter(tamanho=2)
    att2 = att.update(turno='tarde')
    response = Reserva.objects.filter(turno='tarde')

    assert len(response) == len(att)

@pytest.mark.django_db
def test_rmv_agendamento():     #rmv - remover
    dado = Reserva.objects.filter(nome = 'jorge')
    dado.delete()

    assert len(dado) == 0