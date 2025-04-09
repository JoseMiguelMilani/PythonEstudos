idade = int(input('qual sua idade '))

if idade < 18 :
    print('ainda vai se alistar, falta \033[31m{}\033[m anos' .format(18-idade) )
elif idade >= 19 :
    print('ja passou \033[31m{}\033[m anos da hora certa' .format(idade-18))
elif idade == 18:
    print('é a hora')