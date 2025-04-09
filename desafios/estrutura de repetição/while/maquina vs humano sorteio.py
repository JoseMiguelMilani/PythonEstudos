numtot = 0
import random
robo = int(random.randint(1,10))
print(robo)
humano = int(input('escolha um numero de 1 a 10:'))

while humano != robo:
    humano = int(input('errou tente de novo:'))
    numtot += 1

print('o robo tinha escolhido {}'.format(robo))

if numtot == 1:
    print('na mosca')

if numtot <= 4:
    print('foi rapido!! apenas em {} tentativas' .format(numtot))

elif numtot <= 7:
    print('boa!! voce acertou em {} tentativas' .format(numtot))

else:
    print('demorou um pouco, {} tentativas' .format(numtot))

