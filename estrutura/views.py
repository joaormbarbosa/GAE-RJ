from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import RegistroAuditoria

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
