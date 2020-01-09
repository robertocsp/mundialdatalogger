from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        circuitos = []



        with open('/tmp/email-test/EXPORT_1578492012730.csv', 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=';')
            count = 1
            for row in reader:
                count += 1
                if count == 8:
                    circuitos = row
                    break

        csvFile.close()

        for idx, c in enumerate(circuitos, start=1):
            circuito = Circuito()
            circuito.nome = '(' + str(idx) + ') ' + c
            circuito.posicao_coluna = idx
            if c != '':
                circuito.save()
            else:
                print('o index: ' + str(idx) + ' é vazio')


