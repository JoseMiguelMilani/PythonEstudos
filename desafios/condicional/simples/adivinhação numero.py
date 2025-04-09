import random

numeros = [0,1,2,3,4,5]
x = random.choice(numeros)

chute = int(input('qual numero '))

if x == chute :
    print('acertou')
else :
    print('errou era {}'.format(x))