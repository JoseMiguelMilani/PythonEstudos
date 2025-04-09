import random

numeros = [0,1,2,3,4,5]
x = random.choice(numeros)

chute = int(input('qual numero '))

if x == chute :
    print('{}acertou era {}'.format('\033[32m' , x))
else :
    print('{}errou era {}'.format('\033[31m' , x))