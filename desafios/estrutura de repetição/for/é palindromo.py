texto = str(input(''))

texto = texto.replace(' ', '')

texto = texto.lower()

if texto == texto[::-1]:
    print('é palindromo')

else:
    print('não é palindromo')