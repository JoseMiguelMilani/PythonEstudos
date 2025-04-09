maiores = 0
menores = 0

for c in range(0,7):
    idade= int(input('qual sua idade '))

    if idade - 21 >= 0:
        maiores = maiores+1

    if idade - 21 < 0:
        menores = menores+1

print('{} são maiores de idade' .format(maiores))

print('{} são menores de idade' .format(menores))