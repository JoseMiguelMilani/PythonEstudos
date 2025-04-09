num1 = int(input('valor1:'))
num2 = int(input('valor2:'))
acao=0

while acao != 5:
    print('                  ')
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair do programa')
    acao = int(input('qual ação deseja fazer:'))

    if acao == 1:
        print('-='*20)
        print('a soma de \033[32m{}\033[m com \033[32m{}\033[m da \033[33m{}\033[m '.format(num1,num2,(num1+num2) ) )
        print('-='*20)

    if acao == 2:
        print('-='*20)
        print('a multiplicação de \033[32m{}\033[m com \033[32m{}\033[m da \033[33m{}\033[m '.format(num1,num2,(num1*num2) ) )
        print('-='*20)

    if acao == 3:
        if num1 > num2:
            maior = num1

        else:
            maior = num2
        print('-='*20)
        print('O maior é {} ' .format(maior)) 
        print('-='*20)

    if acao == 4:
        num1 = int(input('novos numero1:'))
        num2 = int(input('novos numero2:'))

print('\033[31mencerrado')

