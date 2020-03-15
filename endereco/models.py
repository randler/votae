from django.db import models

# Create your models here.


class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=100, default='Cândido Sales')
    cidade_id = models.TextField()
    estado = models.CharField(max_length=50, default='Bahia')
    estado_id = models.TextField()

    def __str__(self):
        return self.cidade + ', ' + self.estado + ' - ' + self.cep
