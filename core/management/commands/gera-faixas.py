from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Temperatura, Circuito
from datetime import datetime, timedelta



class Command(BaseCommand):
    help = 'Carrega circuitos branch degelodefault'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        circuitos = Circuito.objects.all()

        outputdir = '/tmp/faixas-mdl20.csv'

        with open(outputdir, 'w',  encoding='utf-8', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_ALL)
            for c in circuitos:
                writer.writerow([c.posicao_coluna, c.faixa1, c.faixa2, c.faixa3, c.faixa4, c.faixa5, c.faixa6, c.faixa7, c.faixa8])




