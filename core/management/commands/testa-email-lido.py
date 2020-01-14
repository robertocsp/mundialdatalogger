from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito, Temperatura
from datetime import datetime
from django.utils import timezone



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        def email_ja_lido(email_id, circuito):
            temperatura = Temperatura.objects.filter(id_email=email_id, circuito__loja=circuito.loja)
            if temperatura.exists():
                return True
            else:
                return False

        circuito = Circuito.objects.filter(loja__nome='mdl20').first()
        if email_ja_lido(4, circuito):
            print('email ja lido')
        else:
            print('email ainda nao lido')

