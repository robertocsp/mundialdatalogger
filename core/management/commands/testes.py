from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        DEBUG = os.environ.get('PROJECT_HOMOLOGA', False)
        print(str(DEBUG))
