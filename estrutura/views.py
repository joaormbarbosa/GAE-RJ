from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from django.http import HttpResponse

from .models import RegistroAuditoria


# =========================
# HOME
# =========================
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('https://gae-rj-v-2.onrender.com/')


# =========================
# ADMINISTRATIVO  (único protegido)
# =========================
@login_required
def confirmar_sigilo(request):
    if request.method == 'POST':
        return redirect('bi_administrativo')
    return render(request, 'confirmar_sigilo.html')


@login_required
def bi_administrativo(request):
    contexto = {
        'username': request.user.get_username(),
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi.html', contexto)


# =========================
# BIs PÚBLICOS  (sem login_required)
# =========================
def bi_ebi(request):
    contexto = {
        'username': request.user.get_username() if request.user.is_authenticated else 'Visitante',
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    # Mantive o template que você já usa:
    return render(request, 'bi_EBI.html', contexto)


def bi_visitas(request):
    contexto = {
        'username': request.user.get_username() if request.user.is_authenticated else 'Visitante',
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_visitas.html', contexto)


def bi_musical(request):
    contexto = {
        'username': request.user.get_username() if request.user.is_authenticated else 'Visitante',
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_musical.html', contexto)


def bi_mocidade(request):
    contexto = {
        'username': request.user.get_username() if request.user.is_authenticated else 'Visitante',
        'data_hora': now().strftime('%d/%m/%Y %H:%M:%S'),
    }
    return render(request, 'bi_mocidade.html', contexto)


# =========================
# AUDITORIA
# =========================
@login_required
def auditoria_log(request):
    RegistroAuditoria.objects.create(
        usuario=request.user,
        acao="Copiou conteúdo com Ctrl+C",
    )
    return JsonResponse({'status': 'registrado'})


# =========================
# MAPAS REGIONAIS  (segue com login)
# =========================
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

def healthz(request):
    return HttpResponse("ok")
def formularios(request):
    formularios = [
      
        {
            "nome": "EBI – RPC's",
            "descricao": "Dados para o painel da EBI.",
            "url": "https://forms.cloud.microsoft/r/JmQeKR6yCS"
        },
        {
            "nome": "Pedidos de Visitas",
            "descricao": "Envio de pedidos de visitas.",
            "url": "https://forms.cloud.microsoft/r/5DAva9WsCj"
        },
        {
            "nome": "Visitas Realizadas",
            "descricao": "Envio de dados de visitas realizadas.",
            "url": "https://forms.cloud.microsoft/r/ASZ4e7mVLT"
        },
        {
            "nome": "Musical – GEM",
            "descricao": "Informações dos Grupos de Estudos Musicais.",
            "url": "https://forms.cloud.microsoft/r/RNp3ebHVXA"
        },
        {
            "nome": "Musical – Eventos",
            "descricao": "Informações dos Eventos da Parte Musical",
            "url": "https://forms.cloud.microsoft/r/c19TBeCgYj"
        },
        {
            "nome": "Mocidade - RJM's - Recitativos",
            "descricao": "Coleta de informações dos eventos da mocidade.",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSc_GW_A1POnojKTvn6LAcY-yNCRT_Mq8Msmpt3ztobgaIYN8A/viewform "
        },
        {
            "nome": "Mocidade - Eventos",
            "descricao": "Coleta de informações dos eventos da mocidade.",
            "url": "Em construção"
        },
    ]
    return render(request, 'formularios.html', {"formularios": formularios})