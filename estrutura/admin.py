from django.contrib import admin
from .models import Estado, RegionalAdministrativa, Administracao, Usuario, RegistroAuditoria
from django.contrib.auth.admin import UserAdmin

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(RegionalAdministrativa)
class RegionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    list_filter = ('estado',)

@admin.register(Administracao)
class AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'regional')
    list_filter = ('regional',)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'administracao', 'is_staff', 'is_active')
    list_filter = ('administracao', 'is_staff', 'is_active')

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'data_hora')
    list_filter = ('acao', 'data_hora')
    search_fields = ('usuario__username', 'acao')
    
admin.site.site_header = "GAE-RJ — Administração do Sistema"
admin.site.site_title = "GAE-RJ"
admin.site.index_title = "Painel Administrativo GAE-RJ"
