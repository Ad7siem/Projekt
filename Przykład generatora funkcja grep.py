
import os


path = r'E:\Programowanie\Python\Kurs\Zaawansowany\Projekt'
search_string = 'Ford'
file_extension = '.py'

for dir_name, subdirs, filenames in os.walk(path):
    # print(dir_name, subdirs, filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
           fullFileName = os.path.join(dir_name, filename)
           for line in open(fullFileName, encoding="utf8"):
                if search_string in line:
                    print(filename)


def Generate_Files(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName


def grep_files(search_string, files):
    for file in files:
        with open(file, encoding="utf8") as text:
            if search_string in text.read():
                yield file


file_generator = Generate_Files(path, file_extension)

for file in grep_files(search_string, file_generator):
    print(file)


# ćwiczenia

import os
import requests


def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webrage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


try:
    os.mkdir(r'E:\temp\links_to_check')
except:
    pass

with open(r'E:\temp\links_to_check\pl.txt', 'w') as f:
    f.write('http://wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'E:/temp/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files('E:/temp/links_to_check'):
    for line in gen_get_file_lines(file):
        print('{} - {} - {}'.format(file, line, check_webrage(line)))

