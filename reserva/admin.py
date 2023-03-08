from django.contrib import admin
from reserva.models import Reserva
# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome','nome_pet','telefone','data','turno']
    search_fields = ['nome','nome_pet','telefone']
    list_filter = ['data', 'turno', 'tamanho']