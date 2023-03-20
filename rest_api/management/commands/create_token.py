from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import BaseCommand6

class Command(BaseCommand):
    help = 'Cria um novo token para ser usado'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    def handle(self,*args, **options):
        username = options['username']
        password = options['password']
        self.stdout.write(
            self.style.WARNING(f'Criando Usuário com o nome {username}')
        )
        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'Usuário Criado')
        )
        self.stdout.write(
            self.style.WARNING('Criando um token para o Usuário')
        )
        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token criado para o usuárop: {token.key}')
        )