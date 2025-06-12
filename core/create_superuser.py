from estrutura.models import Usuario

if not Usuario.objects.filter(username='joao.rafael').exists():
    Usuario.objects.create_superuser(
        username='joao.rafael',
        email='joao.rafael@rio.congregacao.org.br',
        password='Zetraxa4@#'
    )
