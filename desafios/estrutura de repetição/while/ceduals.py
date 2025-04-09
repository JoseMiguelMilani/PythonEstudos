valor = cedula50 = cedula20 = cedula10 = cedula1 = divisao = 0
print('=-'*20)
valor = int(input('valor a ser sacado:'))

print('=-'*20)

while valor != 0:
    
    cedula50 = int(valor/50)
    valor = (valor%50)

    if cedula50 > 0:
        print(f'{cedula50} cedulas de 50')



    cedula20 = int(valor/20)
    valor = (valor%20)

    if cedula20 > 0:
        print(f'{cedula20} cedulas de 20')



    cedula10 = int(valor/10)
    valor = (valor%10)

    if cedula10 > 0:
        print(f'{cedula10} cedulas de 10')

        

    cedula1 = int(valor)
    valor = (valor%1)
    if cedula1 > 0:
        print(f'{cedula1} cedulas de 1')


print('=-'*20)





