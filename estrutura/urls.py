from django.urls import path
from . import views
from .views import mapas_regionais

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmar-sigilo/', views.confirmar_sigilo, name='confirmar_sigilo'),
    path('bi-administrativo/', views.bi_administrativo, name='bi_administrativo'),
    path('confirmar-sigilo-musical/', views.confirmar_sigilo_musical, name='confirmar_sigilo_musical'),
    path('bi-musical/', views.bi_musical, name='bi_musical'),
    path('auditoria-log/', views.auditoria_log, name='auditoria_log'),
    path('mapas-regionais/', mapas_regionais, name='mapas_regionais'),
]
