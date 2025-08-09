from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from .models import RegistroAuditoria

# Helper: checar se o usuário está em um grupo
def in_group(user, group_name: str) -> bool:
    return user.is_authenticated and user.groups.filter(name=group_name).exists()

# HOME
@login_required
def home(request):
    u = request.user
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    # Se preferir usar configuração do Django, pode redirecionar para 'login'
    return redirect('https://gae-rj-v-2.onrender.com/')

# ---------------------------
# ADMINISTRATIVO
# ---------------------------
@login_required
def confirmar_sigilo(request):
    if request.method == 'POST':
        return redirect('bi_administrativo')
    return render(request, 'confirmar_sigilo.html')

@login_required
def bi_administrativo(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi.html', contexto)

# ---------------------------
# MOCIDADE
# ---------------------------
@login_required
def confirmar_sigilo_mocidade(request):
    if request.method == 'POST':
        return redirect('bi_mocidade')
    return render(request, 'confirmar_sigilo_mocidade.html')

@login_required
def bi_mocidade(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_mocidade.html', contexto)

# ---------------------------
# MUSICAL
# ---------------------------
@login_required
def confirmar_sigilo_musical(request):
    if request.method == 'POST':
        return redirect('bi_musical')
    return render(request, 'confirmar_sigilo_musical.html')

@login_required
def bi_musical(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_musical.html', contexto)

# ---------------------------
# EBI (novo)
# ---------------------------
@login_required
def confirmar_sigilo_EBI(request):
    if request.method == 'POST':
        return redirect('bi_EBI')
    return render(request, 'confirmar_sigilo_EBI.html')

@login_required
def bi_EBI(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_EBI.html', contexto)

# ---------------------------
# AUDITORIA
# ---------------------------
@login_required
def auditoria_log(request):
    RegistroAuditoria.objects.create(
        usuario=request.user,
        acao="Copiou conteúdo com Ctrl+C"
    )
    return JsonResponse({'status': 'registrado'})

# ---------------------------
# MAPAS REGIONAIS
# ---------------------------
@login_required
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
