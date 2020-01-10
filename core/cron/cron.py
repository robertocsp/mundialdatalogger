import csv
from core.models import Temperatura, Circuito
import imaplib
import email
from datetime import datetime, timedelta
from django.core.management import call_command

def my_scheduled_job():
    call_command('carrega-temperaturas')