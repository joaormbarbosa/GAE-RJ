from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Estado(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class RegionalAdministrativa(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='regionais')

    def __str__(self):
        return f"{self.nome} - {self.estado.nome}"

class Administracao(models.Model):
    nome = models.CharField(max_length=100)
    regional = models.ForeignKey(RegionalAdministrativa, on_delete=models.CASCADE, related_name='administracoes')

    def __str__(self):
        return f"{self.nome} ({self.regional.nome})"

class Usuario(AbstractUser):
    administracao = models.ForeignKey(Administracao, null=True, blank=True, on_delete=models.SET_NULL)

# ✅ Novo modelo adicionado ao final, fora de qualquer outro bloco
class RegistroAuditoria(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    acao = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.acao} em {self.data_hora}"
