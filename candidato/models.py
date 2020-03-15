from django.db import models

# Create your models here.
from endereco.models import Endereco


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
