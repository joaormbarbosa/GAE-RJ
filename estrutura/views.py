from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    usuario = request.user
    return render(request, 'dashboard.html', {'usuario': usuario})
