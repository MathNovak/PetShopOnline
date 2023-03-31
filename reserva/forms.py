from datetime import date
from reserva.models import Reserva
from django import forms
class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para o passado!')
        return data
    
    def clean_date(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        reservas_diarias = Reserva.objects.filter(data=hoje).count()
        if reservas_diarias == 4:
            raise forms.ValidationError(f'O limite de reservas para o dia de hoje ({hoje}) ja excedeu')
        return data
    
    class Meta:
        model = Reserva
        fields = ['nome','nome_pet','telefone','data', 'petshop','turno','tamanho' ,'observacao']