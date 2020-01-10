from django.core.management.base import BaseCommand
import os
#import ezgmail

class Command(BaseCommand):


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #ezgmail.send('80.pereira@gmail.com', 'Teste envio via ezgmail', 'corpo do email')
        print('teste')