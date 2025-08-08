from django.urls import path
from . import views
from .views import mapas_regionais
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmar-sigilo/', views.confirmar_sigilo, name='confirmar_sigilo'),
    path('bi-administrativo/', views.bi_administrativo, name='bi_administrativo'),
    path('confirmar-sigilo-mocidade/', views.confirmar_sigilo_mocidade, name='confirmar_sigilo_mocidade'),
    path('bi-mocidade/', views.bi_mocidade, name='bi_mocidade'),
    path('confirmar-sigilo-musical/', views.confirmar_sigilo_musical, name='confirmar_sigilo_musical'),
    path('bi-musical/', views.bi_musical, name='bi_musical'),
    path('confirmar-sigilo-EBI/', views.confirmar_sigilo_EBI, name='confirmar_sigilo_EBI'),
    path('bi-EBI/', views.bi_EBI, name='bi_EBI'),
    path('auditoria-log/', views.auditoria_log, name='auditoria_log'),
    path('mapas-regionais/', views.mapas_regionais, name='mapas_regionais'),
    path('logout/', views.logout_view, name='logout'),
]
