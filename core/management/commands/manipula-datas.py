from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        circuito = Circuito.objects.get(posicao_coluna=11)
        hora_faixa_1 = circuito.faixa1

        print(str(type(hora_faixa_1)))