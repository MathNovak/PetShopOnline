from django.db import models

class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande'),
    )
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )

    '''ANIMAIS_OPCOES = (
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('coelho','Coelho')
    )'''

    nome = models.CharField(verbose_name='Nome', max_length=50)
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(verbose_name='Telefone:', max_length=20)
    data = models.DateField(verbose_name='Data da reserva', help_text='dd/mm/aaaa')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES, default='não especificado', null=True)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES, null=True)
    observacao = models.TextField(verbose_name='Observação', blank=True)
    petshop = models.ForeignKey('Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
       
    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'

class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)

    def qtd_reservas(self):
        return self.reservas.count()

class CategoriaAnimal(models.Model):
    nome = models.CharField(max_length=100)

    def str(self):
        return self.nome
    
class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_nascimento = models.ForeignKey(CategoriaAnimal, on_delete=models.CASCADE)

    def str(self):
        return self.nome