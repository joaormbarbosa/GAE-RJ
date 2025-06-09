from django.db import models
from django.contrib.auth.models import AbstractUser

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
