from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import RegistroAuditoria
from django.contrib.auth import logout
from django.shortcuts import redirect

# HOME
@login_required
def home(request):
       u = request.user
    contexto = {
        'can_admin': in_group(u, 'Administrativo'),
        'can_musical': in_group(u, 'Musical'),
        'can_mocidade': in_group(u, 'Mocidade'),
        'can_novo': in_group(u, 'NovoDashboard'),
    }
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('https://gae-rj-v-2.onrender.com/')

# ADMINISTRATIVO
@login_required
def confirmar_sigilo(request):
    if request.method == 'POST':
        return redirect('bi_administrativo')
    return render(request, 'confirmar_sigilo.html')

@login_required
@user_passes_test(lambda u: in_group(u, 'Administrativo'))
def bi_administrativo(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S')
    }
    return render(request, 'bi.html', contexto)

# MOCIDADE
@login_required
def confirmar_sigilo_mocidade(request):
    if request.method == 'POST':
        return redirect('bi_mocidade')
    return render(request, 'confirmar_sigilo_mocidade.html')

@login_required
@user_passes_test(lambda u: in_group(u, 'Mocidade'))
def bi_mocidade(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S')
    }
    return render(request, 'bi_mocidade.html', contexto)

# MUSICAL
@login_required
def confirmar_sigilo_musical(request):
    if request.method == 'POST':
        return redirect('bi_musical')
    return render(request, 'confirmar_sigilo_musical.html')

@login_required
@user_passes_test(lambda u: in_group(u, 'Musical'))
def bi_musical(request):
    contexto = {
        'username': request.user.username,
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S')
    }
    return render(request, 'bi_musical.html', contexto)

@login_required
def confirmar_sigilo_EBI(request):
    if request.method == 'POST':
        return redirect('bi_EBI')
    return render(request, 'confirmar_sigilo_EBI.html')

@user_passes_test(lambda u: in_group(u, 'EBI'))
def bi_novo(request):
    ctx = {'username': request.user.username, 'data_hora': now().strftime('%d/%m/%Y %H:%M:%S')}
    return render(request, 'bi_EBI.html', ctx)

# AUDITORIA
@login_required
def auditoria_log(request):
    RegistroAuditoria.objects.create(
        usuario=request.user,
        acao="Copiou conteúdo com Ctrl+C"
    )
    return JsonResponse({'status': 'registrado'})

# MAPAS REGIONAIS (Agora com login_required)
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
