from django.core.management.base import BaseCommand, CommandError
import os
import csv
from core.models import Circuito
from datetime import datetime
from django.utils import timezone



class Command(BaseCommand):
    help = 'Carrega circuitos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('datetime nativo: ' + str(datetime.today()))
        print('datetime timezone: ' + str(timezone.now()))
        print('get Timezone nativo: ' + str(datetime.utcnow()))
