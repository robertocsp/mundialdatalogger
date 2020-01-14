from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Loja(models.Model):
    PVPRO2 = 'p'
    BOSS = 'b'

    DISPOSITIVOS = [
        (PVPRO2, 'Carel Pv Pro2'),
        (BOSS, 'Carel Boss'),
    ]

    #o nome da loja deve ser exatamente a sigla
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    user = models.ManyToManyField(User, related_name='users')
    dispositivo = models.CharField(max_length=1, choices=DISPOSITIVOS, default=PVPRO2)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Conformidade(models.Model):
    nome = models.CharField(max_length=100)
    temp_min = models.FloatField()
    temp_max = models.FloatField()

    def __str__(self):
        return self.nome

class Circuito(models.Model):
    nome = models.CharField(max_length=255)
    posicao_coluna = models.IntegerField(null=True, blank=True)
    conformidade = models.ForeignKey(Conformidade, on_delete=models.CASCADE, default=True)

    #Foi colocado o default como 1, pois normalmente o circuito é carregado automaticamente, para confirmar deve-se ver qual o id do dispositivo
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, default=1)

    faixa1 = models.TimeField(null=True, blank=True)
    faixa2 = models.TimeField(null=True, blank=True)
    faixa3 = models.TimeField(null=True, blank=True)
    faixa4 = models.TimeField(null=True, blank=True)
    faixa5 = models.TimeField(null=True, blank=True)
    faixa6 = models.TimeField(null=True, blank=True)
    faixa7 = models.TimeField(null=True, blank=True)
    faixa8 = models.TimeField(null=True, blank=True)
    tempo_degelo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Temperatura(models.Model):
    datahora = models.DateTimeField(null=True, blank=True)
    temperatura = models.FloatField(null=True, blank=True)
    degelo = models.BooleanField(default=None, null=True, blank=True)
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    id_email = models.IntegerField(default=0)
    arquivo = models.CharField(max_length=255, null=True, blank=True)

    def _get_conformidadae(self):
        if self.temperatura < self.circuito.conformidade.temp_max:
            return 'em conformidade'
        elif self.degelo == False:
            return 'em conformidade'
        else:
            return 'SMS ENVIADO'

    em_conformidade = property(_get_conformidadae)





