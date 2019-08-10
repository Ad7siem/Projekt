import smtplib

def SendInfoEmail (user, password, mailFrom,mailTo,mailSubject,mailBody):

    message2 = '''From: {} 
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)  # tu jest problem

# gdy usunę klamre i mailBody mail zostaje wysłany.
# Teraz skrypt niezadziala. Nie rozumiem co jest nie tak w debbugu ale wydawalo mi sie ze problem z wartoscia str

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
mailBody = '''
Ja wiem, 
Wiem czego chcesz, 
wiem czego brak, 
wiem co bys chcial, 
a mozliwosci do tego brak
'''

user = input('Wprowadź swojego gmaila: ')
password = input('Wprowadź hasło: ')

SendInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody)


