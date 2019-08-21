'''clients = {
    'INFO': 0.5,
    'DATA': 0.2,
    'SOFT': 0.2,
    'INTER': 0.1,
    'OMEGA': 0.0
}



myClient = input("Enter client's name: ").upper()
totalCost = 7200

try:
    ratio = float(input('Enter new ratio: '))
    print('The default % ratio for {} is {}, a new one is {}'.format(myClient, clients[myClient], ratio))
    print('The cost for {} is {}'.format(myClient, ratio * totalCost))
    print('The new ratio in comparison to old ratio: {}'.format(clients[myClient]/ratio))
except KeyError as e:
    print('Client {} is not on the list {}.\nDatalis: {}'.format(myClient, [c for c in clients], e))
except (ValueError, ZeroDivisionError) as e:
    print('There is a problem with entered value for ratio - it must be a number greater than 0.\nDetail: {}'.format(e))
#except ZeroDivisionError as e:
#   print('The new ratio cannot be 0.\nDetail: {}'.format(e))
except Exception as e:
    print('Sorry we have an error...\nDetalis: {}'.format(e))

print('-'*30)
'''
# ćwiczenia

import requests
import os
import shutil

def save_url_to_file(url, file_path):
    r = requests.get(url, stream = True)
    with open(file_path, 'wb') as f:
        f.write(r.content)

url = 'http://www.mobilo24.eu/spis/'
dir = 'E:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError:
    print('Error downloadinf the file. The URL {} is incorrect'.format(url))

except PermissionError:
    print('Error Open File.\nDetalis: ')

except FileNotFoundError:
    print('{} is not exist'.format(tmpfile))

except Exception as e:
    print('Error!!\nDetalis: {}'.format(e))

else:
    print('Download succesfully!')

finally:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('Done')
