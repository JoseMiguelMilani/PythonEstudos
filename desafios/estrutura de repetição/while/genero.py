sexo = str(input('qual o seu genero(M/F)')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('invalido, qual o seu genero(M/F)')).strip().upper()[0]
    

if sexo == 'M':
    print('seu genero é masculino')

else:
    print('seu genero é feminino')