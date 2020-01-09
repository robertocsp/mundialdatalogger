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

        outputdir = '/tmp/faixas-mdl20.csv'

        with open(outputdir, 'r',  encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile, delimiter=';')
            for row in reader:
                circuito = Circuito.objects.get(posicao_coluna=int(row[0]))
                circuito.faixa1 = datetime.strptime(row[1], '%H:%M:%S') if row[1] != '' else None
                circuito.faixa2 = datetime.strptime(row[2], '%H:%M:%S') if row[2] != '' else None
                circuito.faixa3 = datetime.strptime(row[3], '%H:%M:%S') if row[3] != '' else None
                circuito.faixa4 = datetime.strptime(row[4], '%H:%M:%S') if row[4] != '' else None
                circuito.faixa5 = datetime.strptime(row[5], '%H:%M:%S') if row[5] != '' else None
                circuito.faixa6 = datetime.strptime(row[6], '%H:%M:%S') if row[6] != '' else None
                circuito.faixa7 = datetime.strptime(row[7], '%H:%M:%S') if row[7] != '' else None
                circuito.faixa8 = datetime.strptime(row[8], '%H:%M:%S') if row[8] != '' else None
                print(str(circuito.posicao_coluna) + '---' + str(circuito.faixa1))
                circuito.tempo_degelo = 70
                circuito.save()
        csvFile.close()


