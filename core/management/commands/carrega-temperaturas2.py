from django.core.management.base import BaseCommand, CommandError
import csv
from core.models import Temperatura, Circuito, Loja
import imaplib
import email
from datetime import datetime, timedelta
from django.conf import settings

class Command(BaseCommand):
    help = 'Carrega Temperaturas'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        def retorna_circuito_temperatura(arquivo):

            datahora = ''
            temperaturas = []
            circuitos = []
            outputdir = settings.OUTPUTDIR

            with open(outputdir + arquivo, 'r', encoding='utf-8') as csvFile:
                reader = csv.reader(csvFile, delimiter=';')
                count = 1
                for row in reader:
                    count += 1
                    if count == 3:
                        datahora = row[0]
                    if count == 8:
                        circuitos = row
                    if count == 9:
                        temperaturas = row
                        break

            csvFile.close()
            return datahora, temperaturas, circuitos



        def email_ja_lido(email_id, circuito):
            temperatura = Temperatura.objects.filter(id_email=email_id, circuito__loja=circuito.loja)
            if temperatura.exists():
                return True
            else:
                return False


        def downloaAttachmentsInEmail(m, emailid, outputdir):
            filename = ''
            resp, data = m.fetch(emailid, "(BODY.PEEK[])")
            email_body = data[0][1]
            # print(email_body)
            mail = email.message_from_bytes(email_body)

            if mail.get_content_maintype() != 'multipart':
                return
            for part in mail.walk():
                if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                    open(outputdir + part.get_filename(), 'wb').write(part.get_payload(decode=True))
                    return part.get_filename()

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

            if faixa1 != None and (hora_circuito > faixa1 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa1)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa2 != None and (hora_circuito > faixa2 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa2)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa3 != None and (hora_circuito > faixa3 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa3)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa4 != None and (hora_circuito > faixa4 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa4)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa5 != None and (hora_circuito > faixa5 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa5)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa6 != None and (hora_circuito > faixa6 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa6)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa7 != None and (hora_circuito > faixa7 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa7)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            elif faixa8 != None and (hora_circuito > faixa8 and hora_circuito < (
                    (datetime.combine(datetime.today(), temperatura.circuito.faixa8)) + timedelta(0, (
                    tempo_degelo * 60))).time()):
                return True
            else:
                return False


        def retorna_email_id_filename(status, data, mail, outputdir):
            mail_ids = []

            # pega todos os ids
            for block in data:
                mail_ids += block.split()

            # pega o ultimo email e guarda o "id" como count
            count = 1
            ultimo_mail_id = ''
            for i in mail_ids:
                count += 1
                ultimo_mail_id = i

            status, data = mail.fetch(ultimo_mail_id, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    filename = downloaAttachmentsInEmail(mail, ultimo_mail_id, outputdir)
                    return count, filename

        def grava_temperaturas(filename, email_id, circuito_referencia):
            datahora, temperaturas, circuitos = retorna_circuito_temperatura(filename)
            # print(temperaturas)

            # print('email não lido ainda: ' + str(email_id))
            for idx, c in enumerate(temperaturas, start=1):
                if (str(c).strip()) != '':
                    # print(str(c).replace(',', '.'))
                    temperatura = Temperatura()
                    try:
                        temperatura.temperatura = float(str(c).replace(',', '.'))
                    except:
                        temperatura.temperatura = -999.99
                    temperatura.id_email = email_id
                    #tem que informar qual é a loja
                    circuito = Circuito.objects.get(posicao_coluna=idx, loja=circuito_referencia.loja)
                    temperatura.circuito = circuito
                    temperatura.arquivo = filename
                    temperatura.datahora = datetime.strptime(datahora, '%Y-%m-%d %H:%M')
                    if esta_em_degelo(temperatura):
                        temperatura.degelo = True
                        temperatura.temperatura = None
                    else:
                        temperatura.degelo = None
                    temperatura.save()
                    # print(temperatura.datahora)
                    # print('a temperatura do circuito ' + circuito.nome + ' é: ' + str(temperatura.temperatura))

        def ler_emails():
            FROM_EMAIL = "thermoguardian2.ti@gmail.com"  # substitua <seuemail> pelo seu email.
            FROM_PWD = "TRIBUS11"  # substitua <suasenha> pela sua senha
            SMTP_SERVER = "imap.gmail.com"  # padrão
            SMTP_PORT = 993  # padrão
            #outputdir = '/tmp/email-test'
            outputdir = settings.OUTPUTDIR


            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL, FROM_PWD)

            mail.select('inbox', readonly=False)


            #mdl20
            circuito_mdl20 = Circuito.objects.filter(loja__nome='mdl20').first()
            #print(circuito)
            status, data = mail.search(None, 'SUBJECT TESTE')
            email_id, filename = retorna_email_id_filename(status, data, mail, outputdir)

            if not email_ja_lido(email_id, circuito_mdl20):
                grava_temperaturas(filename, email_id, circuito_mdl20)
                #print('email nao lido')
            else:
                print('MDL20 -> email de id: ' + str(email_id) + ' já lido')


            #mdl03
            circuito_mdl03 = Circuito.objects.filter(loja__nome='mdl03').first()
            #print(circuito_mdl03)
            status, data = mail.search(None, 'SUBJECT MDL03TEMP')
            email_id, filename = retorna_email_id_filename(status, data, mail, outputdir)

            if not email_ja_lido(email_id, circuito_mdl03):
                grava_temperaturas(filename, email_id, circuito_mdl03)
                #print('email nao lido')
            else:
                print('MDL03 -> email de id: ' + str(email_id) + ' já lido')


        ler_emails()
