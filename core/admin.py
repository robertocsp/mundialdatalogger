from django.contrib import admin
from . import models
#from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.template.loader import render_to_string
import sys
import csv


@admin.register(models.Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('datahora', 'temperatura', 'degelo', 'em_conformidade', 'circuito',)
    list_filter = [
 #       ('datahora', PastDateRangeFilter),
        ('datahora', DateRangeFilter),
        ('circuito__nome'),

    ]

    list_per_page = sys.maxsize
    actions = ["table_to_html"]

    def circuito(self, instance):
        return instance.circuito.nome

    def table_to_html(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        print(field_names)

        for obj in queryset:
            print(obj)

        pass

    table_to_html.short_description = "Imprimir itens selecionados"




@admin.register(models.Circuito)
class CircuitoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao_coluna', 'faixa1')

@admin.register(models.Conformidade)
class ConformidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'temp_min', 'temp_max',)



