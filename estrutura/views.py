import os  # <<--- IMPORTANTE
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import now

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


# =========================
# FORMULÁRIOS (cards que abrem em nova aba)
# =========================
def formularios(request):
    formularios = [
        {
            "nome": "EBI – RPC's",
            "descricao": "Envio de Informações sobre RPC's - EBI.",
            "url": "https://forms.cloud.microsoft/r/JmQeKR6yCS",
        },
        {   "nome": "Grupo Gestor Construções - CEPI",
            "descrição": "CEPI - Solicitações de apoio as construções e reformas",
             "url": "https://forms.office.com/r/dzuDgCtzfN?embed=true",
        },
        {   "nome": "GAE - Engenharia",
            "descrição": "GAE - Solicitações de Manutenção",
             "url": "https://forms.office.com/r/u513u0SXTW",
        },
        {   "nome": "CAE - Conselho dos Anciães do Estado - RJ",
            "descrição": "CAE - Solicitações ao Conselho dos Anciães",
             "url": "https://forms.office.com/r/Gj1GtpX8ZG",
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
            "descricao": "Informações dos Eventos da Parte Musical.",
            "url": "https://forms.cloud.microsoft/r/c19TBeCgYj",
        },
        {
            "nome": "Mocidade - RJM's - Recitativos",
            "descricao": "Informações dos recitativos das RJM's.",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSc_GW_A1POnojKTvn6LAcY-yNCRT_Mq8Msmpt3ztobgaIYN8A/viewform",
        },
        {
            "nome": "Mocidade - Eventos",
            "descricao": "Informações dos eventos da mocidade.",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSetUtEGTnmaDuIFt82iI7ortzM0ki7RAqeUan9kSCWv7i7Vfw/viewform",
        },
    ]
    return render(request, "formularios.html", {"formularios": formularios})


# =========================
# GESTÃO DE FORMULÁRIOS (somente logado) – links de respostas
# =========================
@login_required
def gestao_formularios(request):
    """Links de RESPOSTAS/ANÁLISES dos formulários (lidos de variáveis de ambiente)."""
    def env_url(key, default=""):
        return (os.environ.get(key) or default).strip()

    itens = [
        # EBI
        {
            "area": "EBI",
            "nome": "EBI – RPC's (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_EBI_RPCS_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&FormId=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUOEtKRE0zUTBUWDdVTE9NRzhXUlZZNUY5Si4u&Token=fea2214db4e5479caeb785e1ac225893"),
        },

        # DARPE e Visitas
        {
            "area": "DARPE e Visitas",
            "nome": "Pedidos de Visitas (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_VISITAS_PEDIDOS_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&FormId=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUMERSSTcyNUczUDhJTElTM0tBQkdKOUlQNC4u&Token=56a513996190410da5f23dddbfc697f2"),
        },
        {
            "area": "DARPE e Visitas",
            "nome": "Visitas Realizadas (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_VISITAS_REALIZADAS_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&token=69c5a461d86541b5b81d1a4d06de4637&id=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUNEU1UzBZV0kyNFJZTzlBRE0yNlBQVDM2Ry4u"),
        },
          {
            "area": "DARPE e Visitas",
            "nome": "Salas de Orações  (Não oficializadas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_SALAS_DE_ORAÇÕES_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&token=e09abb059d8e48c8a6be7dbf977af5e6&id=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUMlhDMkRGMjlCODBHU1Y2UTlQWjZIUVcxQi4u"),
        },

        # Grupo Gestor Construções - CEPI
        {
            "area": "Grupo Gestor Construções - CEPI",
            "nome": "CEPI - Solicitações de apoio as construções e reformas",
            "tipo": "Microsoft Forms",
            "url": env_url("Pedido a CEPI", "https://forms.office.com/Pages/DesignPageV2.aspx?subpage=design&token=e96014b2b7134ba68054c4e71f8596f5&id=f1bn8KykVUe3ClwD-hDjDNSiuJZxpZNNutPXoTAFR4VUNlRBU0QwUzRHSzJSVDFOQVpLRUoxNVpTUS4u"),
        }

        # GAE - Engenharia
        ,
        {
            "area": "GAE - Engenharia",
            "nome": "GAE - Solicitações de Manutenção",
            "tipo": "Microsoft Forms",
            "url": env_url("Análise de Construções e Reformas",
                           "https://forms.office.com/Pages/DesignPageV2.aspx?subpage=design&token=0dd361b1b5ee429ea7b0dfcfbcb5d0a3&id=f1bn8KykVUe3ClwD-hDjDNSiuJZxpZNNutPXoTAFR4VUQTk5WFlWN05ZQkNGNFlBSFpTSEpLV1dTSC4u"),
        }

        # Musical
        {
            "area": "Musical",
            "nome": "Musical – GEM (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_MUSICAL_GEM_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&token=429fa57ed48a440090a6351c454c6e8e&id=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUNjU1UUdKSFFTQjY2VEdFRkFSMUdHNDlDTi4u"),
        },
        {
            "area": "Musical",
            "nome": "Musical – GEM (FIXOS) (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_MUSICAL_GEM_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&token=429fa57ed48a440090a6351c454c6e8e&id=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUNjU1UUdKSFFTQjY2VEdFRkFSMUdHNDlDTi4u"),
        },
        {
            "area": "Musical",
            "nome": "Musical – Eventos (respostas)",
            "tipo": "Microsoft Forms",
            "url": env_url("RESP_MUSICAL_EVENTOS_URL",
                           "https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?subpage=design&FormId=f1bn8KykVUe3ClwD-hDjDB5owopPcwlMmxAga3IXoaZUMjIwR05OQkVWQ0VNUFNLRDdDV05TMlpGTS4u&Token=8e13be9f0708485aa5453deb15ea3db7"),
        },

        # Mocidade (Google Forms)
        {
            "area": "Mocidade",
            "nome": "RJM's - Recitativos (respostas)",
            "tipo": "Google Forms",
            "url": env_url("RESP_MOCIDADE_RJMS_URL", ""),
        },
        {
            "area": "Mocidade",
            "nome": "Mocidade - Eventos (respostas)",
            "tipo": "Google Forms",
            "url": env_url("RESP_MOCIDADE_EVENTOS_URL", ""),
        },
    ]

    itens = [i for i in itens if i["url"]]
    return render(request, "gestao_formularios.html", {"itens": itens})
