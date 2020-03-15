from django.db import models

from candidato.models import Candidato
from endereco.models import Endereco

# Create your models here.


class Voto(models.Model):
    class Meta:
        verbose_name = 'Voto'

    cpf = models.CharField(max_length=14, unique=True)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf
