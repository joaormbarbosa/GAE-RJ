from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import RegistroAuditoria
from django.shortcuts import render

# TELA INICIAL
@login_required
def home(request):
    return render(request, 'home.html')

# TELA DE CONFIRMAÇÃO DE SIGILO
@login_required
def confirmar_sigilo(request):
    if request.method == 'POST':
        return redirect('bi_dashboard')
    return render(request, 'confirmar_sigilo.html')

# TELA DO DASHBOARD BI (com username e data_hora para alertas e marca d'água)
@login_required
def bi_dashboard(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S')
    }
    return render(request, 'bi.html', contexto)

# REGISTRO DE AUDITORIA (ao tentar copiar conteúdo)
@login_required
def auditoria_log(request):
    RegistroAuditoria.objects.create(
        usuario=request.user,
        acao="Copiou conteúdo com Ctrl+C"
    )
    return JsonResponse({'status': 'registrado'})

# TELA CHECKLIST GERAL
@login_required
def checklist_geral(request):
    return render(request, 'checklist.html', {
        'usuario': request.user
    })


def mapas_regionais(request):
    mapas = [
        {'nome': 'Angra dos Reis', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-angra-dos-reis_1076926'},
        {'nome': 'Duque de Caxias', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-duque-de-caxias_1076927'},
        {'nome': 'Itaperuna', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-itaperuna_1077482'},
        {'nome': 'Macaé', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-macae_1075040'},
        {'nome': 'Nova Friburgo', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-nova-friburgo_1081420'},
        {'nome': 'Nova Iguaçu', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-nova-iguacu_1085973'},
        {'nome': 'Resende', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-resende_1075043'},
        {'nome': 'Rio de Janeiro', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-rio-de-janeiro_1072743'},
        {'nome': 'São Gonçalo', 'url': 'https://umap.openstreetmap.fr/pt-br/map/regional-sao-goncalo_1075017'},
    ]

    mapa_url = request.GET.get("mapa")
    mapa_nome = next((m["nome"] for m in mapas if m["url"] == mapa_url), None)

    context = {
        "mapas": mapas,
        "mapa_selecionado": mapa_url,
        "mapa_nome": mapa_nome,
    }
    return render(request, "mapas_regionais.html", context)
