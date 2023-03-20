from django.urls import path,include
from rest_api.views import reservas, adicionar_reserva, AgendamentoModelViewSet
from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)

urlpatterns = [
    path('reservas/', reservas, name='reservas'),
    path('adicionar_reserva/', adicionar_reserva, name='adicionar_reserva'),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls