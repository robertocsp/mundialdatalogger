from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito, Loja



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        loja = Loja.objects.get(pk=3)

        circuitos = []

        with open('/tmp/email-test/EXPORT_1579032013395.csv', 'r') as csvFile:
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
            circuito.loja = loja

            if c != '':
                circuito.save()
                #print('circuito: ' + circuito.nome + ' --- Loja: ' + circuito.loja.nome)
            else:
                print('o index: ' + str(idx) + ' é vazio')


