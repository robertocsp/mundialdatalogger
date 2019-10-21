from django.contrib import admin
from . import models
from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter


@admin.register(models.Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('datahora', 'temperatura', 'degelo','circuito', 'arquivo', 'id_email')
    list_filter = [
        ('datahora', PastDateRangeFilter),
        ('circuito__nome'),

    ]

    def circuito(self, instance):
        return instance.circuito.nome

@admin.register(models.Circuito)
class CircuitoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao_coluna')



