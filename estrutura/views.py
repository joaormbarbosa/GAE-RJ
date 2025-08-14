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

def home(request):
    return render(request, 'home.html')



def logout_view(request):
    logout(request)
    return redirect('home')


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
# MAPAS REGIONAIS  
# =========================

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
    itens = [
        {
            "nome": "EBI – RPC's",
            "descricao": "Envio de Informações sobre RPC's - EBI.",
            "url": "https://forms.cloud.microsoft/r/JmQeKR6yCS",
        },
        {
            "nome": "Pedidos de Visitas",
            "descricao": "Envio de pedidos de visitas.",
            "url": "https://forms.cloud.microsoft/r/5DAva9WsCj",
        },
        {
            "nome": "Visitas Realizadas",
            "descricao": "Envio sobre as visitas realizadas.",
            "url": "https://forms.cloud.microsoft/r/ASZ4e7mVLT",
        },
        {
            "nome": "Musical – GEM",
            "descricao": "Informações dos Grupos de Estudos Musicais.",
            "url": "https://forms.cloud.microsoft/r/RNp3ebHVXA",
        },
        {
            "nome": "Musical – Eventos",
            "descricao": "Informações dos Eventos da Parte Musical",
            "url": "https://forms.cloud.microsoft/r/c19TBeCgYj",
        },
        {
            "nome": "Mocidade - RJM's - Recitativos",
            "descricao": "Informações dos recitativos das RJM's.",
            # use o link COMPLETO do Google Forms (docs.google.com/forms/.../viewform)
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSc_GW_A1POnojKTvn6LAcY-yNCRT_Mq8Msmpt3ztobgaIYN8A/viewform",
        },
        {
            "nome": "Mocidade - Eventos",
            "descricao": "Informações dos eventos da mocidade.",
            # substitua forms.gle por docs.google.com/forms/.../viewform para embutir
            "url": "https://docs.google.com/forms/d/e/SEU_FORM_ID/viewform",
        },
    ]

    def make_embed(u: str):
        u = u.strip()
        # Microsoft Forms
        if ("forms.office.com" in u) or ("forms.microsoft.com" in u) or ("forms.cloud.microsoft" in u):
            return u + ("&" if "?" in u else "?") + "embed=true"
        # Google Forms (link completo do docs.google.com/forms)
        if "docs.google.com/forms" in u:
            return u + ("&" if "?" in u else "?") + "embedded=true"
        # Não embutível (ex.: forms.gle curto)
        return None

    for f in itens:
        base = f["url"].strip()
        f["open_url"] = base
        f["embed_url"] = make_embed(base)

    form_url = request.GET.get("form")  # recebemos a embed_url
    form_nome = next((i["nome"] for i in itens if i["embed_url"] == form_url), None)
    open_url = next((i["open_url"] for i in itens if i["embed_url"] == form_url), None)

    context = {
        "formularios": itens,
        "form_selecionado": form_url,
        "form_nome": form_nome,
        "form_open_url": open_url,
    }
    return render(request, "formularios.html", context)
