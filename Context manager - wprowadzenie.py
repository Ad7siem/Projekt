'''
try:
    with open(r'E:\temp\my_file*.txt', 'w+') as file:
        file.writelines('SUCCESS')
except OSError as e:
    print('Error opening the file {}, details: {}'.format(e.filename, e.strerror))
'''

import time


class time_measure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering...')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))


with time_measure() as my_timer:
    time.sleep(0)

print('-'*30,'\n')
# ćwiczenia


class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        return print('''
<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>            
        ''')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')

with HtmlCM() as my_html:
    print('''
 <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>
    ''')