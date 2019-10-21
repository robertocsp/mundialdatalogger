from django.db import models

# Create your models here.
class Circuito(models.Model):
    nome = models.CharField(max_length=100)
    posicao_coluna = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Temperatura(models.Model):
    datahora = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField()
    degelo = models.BooleanField(default=False)
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    id_email = models.IntegerField(default=0)
    arquivo = models.CharField(max_length=255, null=True, blank=True)



