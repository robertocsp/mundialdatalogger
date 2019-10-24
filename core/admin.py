import datetime

from django.contrib import admin, messages
from django.core.exceptions import TooManyFieldsSent
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from openpyxl import Workbook

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
        # ('datahora', PastDateRangeFilter),
        ('datahora', DateRangeFilter),
        'circuito__nome',

    ]

    # list_per_page = sys.maxsize
    list_per_page = 999
    actions = ['table_to_html', 'export_excel']

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

    def export_excel(self, request, queryset):
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename={date}-temperaturas.xlsx'.format(
            date=datetime.datetime.now().strftime('%Y-%m-%d'),
        )
        workbook = Workbook()

        # Get active worksheet/tab
        worksheet = workbook.active
        worksheet.title = 'Temperaturas'

        # Define the titles for columns
        columns = [
            'Datahora',
            'Temperatura',
            'Degelo',
            'Em conformidade',
            'Circuito',
        ]
        row_num = 1

        # Assign the titles for each cell of the header
        for col_num, column_title in enumerate(columns, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title

        # Iterate through all movies
        for item in queryset:
            row_num += 1

            # Define the data for each cell in the row
            row = [
                item.datahora,
                item.temperatura,
                item.degelo,
                item.em_conformidade,
                item.circuito.nome,
            ]

            # Assign the data for each cell of the row
            for col_num, cell_value in enumerate(row, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = cell_value

        workbook.save(response)

        return response

    export_excel.short_description = "Exportar para Excel itens selecionados"


@admin.register(models.Circuito)
class CircuitoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao_coluna', 'faixa1')


@admin.register(models.Conformidade)
class ConformidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'temp_min', 'temp_max',)
