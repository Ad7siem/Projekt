var_x = 10

source = '''
new_var = 1
for i in range(var_x):
    print('x'*i)
    new_var += i
'''

result = exec(source) # wykonuje kod, nie zwraca wartosci
print(result)

print(var_x)
print(new_var)

source = input('Enter your expression: ')
print(eval(source))

# ćwiczenia

files_to_process = [
    r'D:\temp\script 1.py',
    r'D:\temp\script 2.py'
]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print('File {} ...'.format(file_path))
        source = f.read()
        exec(source)