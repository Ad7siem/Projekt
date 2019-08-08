instruction = ['say hello', 'say how are you', 'ask for money','say thank you','say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:',instr)
    instructionApproved.append(instr)

print('Follwing actions will be taken', instructionApproved)

print('#####################################','\n')

instruction = ['say hello', 'say how are you','abort', 'ask for money','say thank you','say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:',instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!!')
        instructionApproved.clear()
        break
else:
    print('Follwing actions will be taken', instructionApproved)

print('-'*30)
instructionApproved.clear()
i = 0
while i < len(instruction):
    print('Adding instruction:',instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!')
        instructionApproved.clear()
        break

    i += 1
else:
    print('Follwing actions will be taken', instructionApproved)

# ćwiczenia

import os
import urllib.request

data_dir = r'D:\temp'
pages = [
    {'name':'mobilo', 'url':'http://www.mobilo24.eu/'},
    {'name':'nonexistent','url':'http://abc.cde.fgh.ijk.pl/'},
    {'name':'kursy','url':'http://www.kursyonline24.eu/'}]

for page in pages:
    try:
        file_name = '{}.html'.format(page['name'])
        path = os.path.join(data_dir,file_name)
        print('Processing: {} => {} ...'.format(page['url'],file_name))
        urllib.request.urlretrieve(page['url'],path)
        print('...done')

    except:
        print('FAILURE processing web page: {}'.format(page['name']))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')