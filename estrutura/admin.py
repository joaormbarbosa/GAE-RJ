from django.contrib import admin
from .models import Estado, RegionalAdministrativa, Administracao, Usuario, RegistroAuditoria
from django.contrib.auth.admin import UserAdmin

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(RegionalAdministrativa)
class RegionalAdministrativaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    search_fields = ('nome',)
    list_filter = ('estado',)

@admin.register(Administracao)
class AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'regional')
    search_fields = ('nome',)
    list_filter = ('regional',)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('administracao',)}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active', 'administracao')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'administracao')

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'data_hora')
    search_fields = ('usuario__username', 'acao')
    list_filter = ('data_hora',)
