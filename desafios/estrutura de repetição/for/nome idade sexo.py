velho = 0
idade = 0
mulheres = 0
media = 0
oma = ''

for i in range (0, 4):

    print('-----{} pessoa-----' .format(i+1))
    nome = str(input('nome:')).strip()
    idade = int(input('idade:'))
    sexo = int(input('sexo(1 para homem, 2 para mulher):'))

    media += idade

    if sexo == 1 and idade > velho:
        oma = nome
        velho = idade
        

    if idade < 20 and sexo == 2:
        mulheres += 1


media = media/4

print('o homem mais velho é {} com {} anos' .format(oma, velho))
print('a media de idade é {} anos' .format(media))
print('existem {} mulheres abaixo de 20 anos' .format(mulheres))