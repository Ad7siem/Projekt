myvar = 'Hello Pycharm!'
myvar2 = myvar + '!!'
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is Calue the same?', myvar==myvar2) # czy obie zmienne maja taka sama wartosc
print('Are the variables the same?', myvar is myvar2) # czy cos po lewej jest to samo co po prawej
print(id(myvar),id(myvar2))
myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is Calue the same?', myvar==myvar2) # czy obie zmienne maja taka sama wartosc
print('Are the variables the same?', myvar is myvar2) # czy cos po lewej jest to samo co po prawej
print(id(myvar),id(myvar2))
print('#########################################','\n')

# ćwiczenia

a = b = c = 10
print(a,b,c)
print(id(a),id(b),id(c))

a = 20
print(a,b,c)
print(id(a),id(b),id(c))
print('#########################################','\n')

a = b = c = ['1','2','3']
a.append(4)
print(a,b,c)
print(id(a),id(b),id(c))
print('#########################################','\n')

x = 10
y = 10
print(id(x),id(y))
print('#########################################','\n')
y = y + 1 - 1
print(id(x),id(y))
print('#########################################','\n')

y = y + 1234567890 - 1234567890
print(id(x),id(y))
