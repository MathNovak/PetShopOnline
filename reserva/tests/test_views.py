from pytest_django.asserts import assertTemplateUsed
import pytest
from model_bakery import baker
from datetime import date, timedelta

from reserva.models import Reserva, Petshop



'''def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')'''

@pytest.mark.django_db
def test_reserva_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'jao',
        'email': 'jao@email.com',
        'nome_pet': 'meg',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacao': 'meg é mt raivosa'
    }
    response = client.post('/reserva/criar/', dados)

    assert response.status_code == 200
    assert 'Reserva realizada com sucesso, em breve entraremos em contato!' in str (response.content)
