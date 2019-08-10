import smtplib
import email

mailFrom = 'Your automatic system'
mailTo = ['Ad_siem@windowslive.com', 'ad7siem@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''
Ja wiem, 
Wiem czego chcesz, 
wiem czego brak, 
wiem co bys chcial, 
a możliwości do tego brak''' # encoding utf-8

message2 = '''From: {} 
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)  # tu jest problem

# gdy usunę klamre i mailBody mail zostaje wysłany.
# Teraz skrypt niezadziala. Nie rozumiem co jest nie tak w debbugu ale wydawalo mi sie ze problem z wartoscia str

user = input('Wprowadź swojego gmaila: ')
password = input('Wprowadź hasło: ')

message = 'Sprawdzam'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # takiego klienta potrzebuje gmail (SMTP_SSL)
    server.ehlo()  # przywitanie sie z serwerem - przesyla informacje o komputerze z ktoego jest wysylany mail
    server.login(user, password)
    server.sendmail(user, mailTo, message2)
    server.close()
    print('mail sent')
except:
    print('Error sending email')
