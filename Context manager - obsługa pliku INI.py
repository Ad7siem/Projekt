import os


class ini_file:

    def __init__(self, path):
        print('__init__')
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace('\n', '').split('=')
                    self.parameters[parts[0]] = parts[1]

    def read_parameter(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameter(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():
                line = '{}={}\n'.format(key, value)
                file.writelines(line)

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        pass


ini = ini_file(r'E:\temp\my.ini')
ini.write_parameter('version', 1)
ini.write_parameter('level', 'advanced')
ini.save_on_disk()

ini2 = ini_file(r'E:\temp\my.ini')
print(ini2.parameters)
print(ini2.read_parameter('version'))
print(ini2.read_parameter('level'))

with ini_file(r'E:\temp\my.ini') as ini3:
    print(ini3.parameters)
    print(ini3.read_parameter('version'))
    print(ini3.read_parameter('level'))

print('-' * 30)

# ćwiczenia

import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as file:
            file.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        z_file = z.namelist()[0]
        print(z_file)
        os.chdir(r'E:\temp\wypakowane pliki zip')
        z.extract(z_file, '.', None)
'''
zrozumiec zapamietac wykorzystywac
'''