jogador = computador = numerosDeJogada = numero = parimpar = 0


import random

while True:
    
    computador = random.randint(1,5)
    jogador = int(input('par ou impar?[1]par [2]impar '))
    numero = int(input('digite um numero de 1 a 5:'))

    parimpar = (computador+numero)%2

    if jogador != parimpar+1:
        print('\033[33merrou\033[m')
        break

    else:
        print('\033[32macertou\033[m')

    numerosDeJogada += 1

print(f'\033[32mvoce conseguiu {numerosDeJogada} vitorias\033[m')