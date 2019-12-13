from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito
import datetime



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print(str(datetime.datetime.today()))