nt1 = float(input('nota 1 '))

nt2 = float(input('nota 2 ' ))

media = (nt1+nt2)/2

print('\033[33m{}\033[m' .format(media))

if media < 5:
    print('reprovou')

elif media >= 7 :
    print('passou')

else :
    print('recuperação')