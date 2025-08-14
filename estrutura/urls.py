from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # BI Administrativo (único com confirmação de sigilo)
    path('confirmar-sigilo/', views.confirmar_sigilo, name='confirmar_sigilo'),
    path('bi-administrativo/', views.bi_administrativo, name='bi_administrativo'),

    # BIs PÚBLICOS
    path('bi-ebi/', views.bi_ebi, name='bi_ebi'),
    path('bi-visitas/', views.bi_visitas, name='bi_visitas'),
    path('bi-musical/', views.bi_musical, name='bi_musical'),
    path('bi-mocidade/', views.bi_mocidade, name='bi_mocidade'),

    # Outros
    path('auditoria-log/', views.auditoria_log, name='auditoria_log'),
    path('mapas-regionais/', views.mapas_regionais, name='mapas_regionais'),
    
    # Formulários (página de links)
    path('formularios/', views.formularios, name='formularios'),

    # Auth
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # (se ainda não tiver em outro arquivo)
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('healthz/', views.healthz, name='healthz'),
    
]
