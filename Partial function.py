"""import smtplib
import functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message2 = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)  # encoding utf-8

    message = 'Sprawdzam'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # takiego klienta potrzebuje gmail (SMTP_SSL)
        server.ehlo()  # przywitanie sie z serwerem - przesyla informacje o komputerze z ktoego jest wysylany mail
        server.login(user, password)
        server.sendmail(user, mailTo, message2)
        server.close()
        print('mail sent')
        return True
    except:
        print('Error sending email')
        return False


mailFrom = 'Your automatic system'
mailTo = ['Ad_siem@windowslive.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Dziala?
Ja wiem,
Wiem czego chcesz,
wiem czego brak,
wiem co bys chcial,
a mozliwosci do tego brak'''  # encoding utf-8

user = input('Wprowadź swojego @gmail.com:')
password = input('Wprowadź hasło: ')

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)

SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)

# SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
"""

# ćwiczenia

import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, dir='D:/temp/', msg='Please wait: {}')


url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url = url, file = file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'D:/temp/'
file = 'logo.png'
save_url_to_dir(url = url, file = file)
