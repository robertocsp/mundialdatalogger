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

        def esta_em_degelo(temperatura):
            tempo_degelo = temperatura.circuito.tempo_degelo
            hora_circuito = temperatura.datahora.time()

            faixa1 = temperatura.circuito.faixa1
            faixa2 = temperatura.circuito.faixa2
            faixa3 = temperatura.circuito.faixa3
            faixa4 = temperatura.circuito.faixa4
            faixa5 = temperatura.circuito.faixa5
            faixa6 = temperatura.circuito.faixa6
            faixa7 = temperatura.circuito.faixa7
            faixa8 = temperatura.circuito.faixa8

            if faixa1 != None and (hora_circuito > faixa1 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa1)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa2 != None and (hora_circuito > faixa2 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa2)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa3 != None and (hora_circuito > faixa3 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa3)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa4 != None and (hora_circuito > faixa4 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa4)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa5 != None and (hora_circuito > faixa5 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa5)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa6 != None and (hora_circuito > faixa6 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa6)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa7 != None and (hora_circuito > faixa7 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa7)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            elif faixa8 != None and (hora_circuito > faixa8 and hora_circuito < ((datetime.combine(datetime.today(), temperatura.circuito.faixa8)) + timedelta(0, (tempo_degelo * 60))).time()):
                return True
            else:
                return False

        temperaturas = Temperatura.objects.all()
        count = 0
        for t in temperaturas:
            count += 1
            if esta_em_degelo(t):
                t.degelo = True
                t.save()
                print('setou degelo=True' + str(count))
            else:
                t.degelo = False
                t.save()
                print('setou degelo=True' + str(count))


