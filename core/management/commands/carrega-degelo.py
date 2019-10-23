from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito
from datetime import datetime, timedelta



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        circuitos = Circuito.objects.all()
        for c in circuitos:
            c.faixa1 = datetime.strptime('2019-10-22 01:00', '%Y-%m-%d %H:%M').time()
            c.faixa2 = datetime.strptime('2019-10-22 05:00', '%Y-%m-%d %H:%M').time()
            c.faixa3 = datetime.strptime('2019-10-22 09:00', '%Y-%m-%d %H:%M').time()
            c.faixa4 = datetime.strptime('2019-10-22 13:00', '%Y-%m-%d %H:%M').time()
            c.faixa5 = datetime.strptime('2019-10-22 17:00', '%Y-%m-%d %H:%M').time()
            c.faixa6 = datetime.strptime('2019-10-22 21:00', '%Y-%m-%d %H:%M').time()
            c.tempo_degelo = 70

            c.save()



