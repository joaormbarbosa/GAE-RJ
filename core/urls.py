from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from estrutura import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),
    path('dashboard/confirmar/', views.confirmar_sigilo, name='confirmar_sigilo'),
    path('dashboard/bi/', views.bi_dashboard, name='bi_dashboard'),
    path('auditoria/log/', views.auditoria_log, name='auditoria_log'),
    path('checklist/', views.checklist_geral, name='checklist_geral'),

]
