import csv
from core.models import Temperatura, Circuito
import imaplib
import email
from datetime import datetime, timedelta

def my_scheduled_job():

    def retorna_circuito_temperatura(arquivo):
        datahora = ''
        temperaturas = []
        circuitos = []
        outputdir = '/tmp/email-test/'

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

    def email_ja_lido(email_id):
        temperatura = Temperatura.objects.filter(id_email=email_id)
        #print('chegou na funcao email_ja_lido, resultado de exists: ' + str(temperatura.exists()))
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
                open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))
                return part.get_filename()


    def ler_email():
        FROM_EMAIL = "thermoguardian.ti@gmail.com"  # substitua <seuemail> pelo seu email.
        FROM_PWD = "TRIBUS11"  # substitua <suasenha> pela sua senha
        SMTP_SERVER = "imap.gmail.com"  # padrão
        SMTP_PORT = 993  # padrão
        outputdir = '/tmp/email-test'

        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)

        mail.select('inbox', readonly=False)

        status, data = mail.search(None, 'SUBJECT TESTE')

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

        # pega o último elemento
        # ultimo_mail_id = mail_ids[-1]
        # lista_enumerada_emails = enumerate(mail_ids)

        status, data = mail.fetch(ultimo_mail_id, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                filename = downloaAttachmentsInEmail(mail, ultimo_mail_id, outputdir)
                return count, filename

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

    email_id, filename = ler_email()
    # print(email_id)
    # email_id_inteiro = int.from_bytes(email_id)
    #print('email_id: ' + str(email_id) + '  ---  ' + str(filename))

    if not email_ja_lido(email_id):

        datahora, temperaturas, circuitos = retorna_circuito_temperatura(filename)

        #print('entrou na funcao email_ja_lido')

        #print('email não lido ainda')
        for idx, c in enumerate(temperaturas, start=1):
            if (str(c).strip()) != '':
                # print(str(c).replace(',', '.'))
                temperatura = Temperatura()
                temperatura.temperatura = float(str(c).replace(',', '.'))
                temperatura.id_email = email_id
                # circuito = Circuito.objects.filter(nome__contains=circuitos[idx]).first()
                circuito = Circuito.objects.get(posicao_coluna=idx)
                temperatura.circuito = circuito
                temperatura.arquivo = filename
                temperatura.datahora = datetime.strptime(datahora, '%Y-%m-%d %H:%M')
                if esta_em_degelo(temperatura):
                    temperatura.degelo = False
                else:
                    temperatura.degelo = True
                temperatura.save()
                #print('a temperatura do circuito ' + circuito.nome + ' é: ' + str(temperatura.temperatura))
    else:
        print('email de id: ' + str(email_id) + ' já lido')

print('Job finalizado Django crontab')