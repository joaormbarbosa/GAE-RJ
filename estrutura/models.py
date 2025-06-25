from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Estado(models.Model):
    nome = models.CharField("Nome do Estado", max_length=100)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nome

class RegionalAdministrativa(models.Model):
    nome = models.CharField("Nome da Regional", max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='regionais')

    class Meta:
        verbose_name = "Regional Administrativa"
        verbose_name_plural = "Regionais Administrativas"

    def __str__(self):
        return f"{self.nome} - {self.estado.nome}"

class Administracao(models.Model):
    nome = models.CharField("Nome da Administração", max_length=100)
    regional = models.ForeignKey(RegionalAdministrativa, on_delete=models.CASCADE, related_name='administracoes')

    class Meta:
        verbose_name = "Administração"
        verbose_name_plural = "Administrações"

    def __str__(self):
        return f"{self.nome} ({self.regional.nome})"

class Usuario(AbstractUser):
    administracao = models.ForeignKey(Administracao, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

# Registro de Auditoria
class RegistroAuditoria(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    acao = models.CharField("Ação", max_length=100)
    data_hora = models.DateTimeField("Data e Hora", auto_now_add=True)

    class Meta:
        verbose_name = "Registro de Auditoria"
        verbose_name_plural = "Registros de Auditoria"

    def __str__(self):
        return f"{self.usuario.username} - {self.acao} em {self.data_hora}"
