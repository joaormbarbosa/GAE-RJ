
import os
from estrutura.models import Usuario

senha = os.environ.get('SUPERUSER_PASSWORD')

if senha and not Usuario.objects.filter(username='admin').exists():
    Usuario.objects.create_superuser(
        username='admin',
        email='joao.rafael@rio.congregacao.org.br',
        password=senha

    )
