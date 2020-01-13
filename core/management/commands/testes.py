from django.core.management.base import BaseCommand
import os
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #call_command('testadata')
        #os.environ['TESTEENV'] = 'True'
        print(settings.OUTPUTDIR)

