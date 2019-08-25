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
        print('exc_type={}'.format(exc_type))
        print('exc_val={}'.format(exc_val))
        print('exc_tb={}'.format(exc_tb))
        if exc_type == OSError:
            return False
        else:
            return True


with ini_file(r'E:\temp\my.ini') as myini:
    myini.write_parameter('mode', 'strict')
    myini.write_parameter('loglevel', 'light')
    myini.save_on_disk()
    print(10/0)


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
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError or KeyError:
            print('exc_type={}'.format(exc_type))
            print('exc_val={}'.format(exc_val))
            return True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r'E:\temp\wypakowane pliki zip')
        z.extract(a_file, '.', None)
