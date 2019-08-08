#import os
'''
path = r'd:\temp\mydata.txt'

#os.remove(path)

if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('Creating a file %s' % path)
    open(path,'x').close()
    print('File %s created' % path)

result = os.path.isfile(path) or open(path,'x').close() # bez bledu wystapi tylko gdy jest or. w przypadku and a plik istnieje wystapi blad w drugim warunku
print(result)
print('#################################################','\n')
'''
# ćwiczenia

'''
def CountWords(file):
    with open(file,'r', encoding='utf-16') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count

file = r'd:\temp\text.txt'
#open(file,'x').close()
if os.file.isfile((file)):
    print('There are {} words in the file {}'.format(CountWords(file),file))

os.file.isfile(file) and print('There are {} words in the file {}'.format(CountWords(file),file))
'''
import os


def CountWords(path):
    with open(path, 'r', encoding='utf-16') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


path = r'c:\temp\test.txt'
if os.path.isfile(path):
    print("There are {} words in the file {}".format(CountWords(path), path))

os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))