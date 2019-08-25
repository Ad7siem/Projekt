class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print('Opening door to the {}'.format(self.where))

    def close(self):
        print('Closing door to the {}'.format(self.where))


door1 = Door('Hell')
door2 = Door('Future')

door1.open()
door1.close()
door2.open()
door2.close()

print('-' * 30)

from contextlib import contextmanager

'''
@contextmanager
def OpenAndClose(obj):
    obj.open()
    yield obj
    obj.close()


with OpenAndClose(Door('next room')) as door:
    print('the dore is to the {}'.format(door.where))
'''
'''
@contextmanager
def Close(obj):
    yield obj
    obj.close()


with Close(Door('next room')) as door:
    door.open()
    print('the dore is to the {}'.format(door.where))
'''

'''
from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line)
'''
'''
import os

#os.remove(r'E:\temp\cos.txt')

from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove(r'E:\temp\cos.txt')
'''

from contextlib import redirect_stdout

f = open(r'E:\temp\cos.txt', 'w')
with redirect_stdout(f):
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()

print('-'*30)

# ćwiczenia

import os
import zipfile
import requests
import contextlib


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        if os.path.isfile(self.tmp_file):
            os.remove(self.tmp_file)


#f = FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref1.zip')
#f.download_file()

with contextlib.suppress(FileNotFoundError):

    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/temp/euroxref1.zip')) as f:
        f.download_file()

        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(r'E:\temp\wypakowane pliki zip')
            z.extract(a_file, '.', None)

        os.remove(f.tmp_file)
