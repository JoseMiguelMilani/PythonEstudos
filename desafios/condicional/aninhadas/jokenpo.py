from random import randint


itens = ('pedra', 'papel', 'tesoura ')

comp = randint(0,2)

jog = int(input('pedra=0, papel=1, tesoura=2 '))

print('{}' .format('-'*20))

print('computador :\033[31m{}'.format(itens[comp]))
print('\033[mvoce: \033[32m{}'.format(itens[jog]))

print('\033[m{}' .format('-'*20))


if comp == 0:
    if jog == 0:
        print('\033[33mempate')

    elif jog == 1:
        print('\033[32mjogador venceu')


    elif jog == 2:
        print('\033[31mcomputador venceu')


    else:
        print('\033[31mjogada invalida')


elif comp == 0:
    if jog == 0:
        print('\033[31mcomputador venceu')

    elif jog == 1:
        print('\033[33mempate')

    elif jog == 2:
        print('\033[32mjogador venceu')

    else:
        print('\033[31mjogada invalida')

elif comp == 0:
    if jog == 0:
        print('\033[32mjogador venceu')

    elif jog == 1:
        print('\033[31mcomputador venceu')

    elif jog == 2:
        print('\033[33mempate')

    else:
        print('\033[31mjogada invalida')