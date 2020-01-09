import csv
from core.models import Temperatura, Circuito
import imaplib
import email
from datetime import datetime, timedelta

def my_scheduled_job():
    print('Job finalizado Django crontab')