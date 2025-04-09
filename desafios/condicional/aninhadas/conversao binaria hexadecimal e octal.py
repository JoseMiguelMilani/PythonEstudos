num = int(input('qual o numero inteiro \033[32m'))
base = str(input('\033[m qual base numerica?\033[31m binario, ocatal, hexadecimal?  \033[32m'))

if base == ('binario') :
    res = bin(num) [2:]

elif base == ('hexadecimal') :
    res = hex(num) [2:]

elif base == ('octal') :
    res = oct(num) [2:]

print('\033[32m{}' .format(res))