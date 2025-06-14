from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmar-sigilo/', views.confirmar_sigilo, name='confirmar_sigilo'),
    path('checklist/', views.checklist_geral, name='checklist_geral'),
    path('bi/', views.bi_dashboard, name='bi_dashboard'),
    path('auditoria-log/', views.auditoria_log, name='auditoria_log'),
]
