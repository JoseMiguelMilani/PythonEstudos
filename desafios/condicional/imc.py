alt = float(input('sua altura'))
pes = float(input('seu peso'))

imc = pes/(alt**2)

print ('seu imc é {:.2f}' .format(imc))

if imc <= 18.5:
    print('abaixo do peso')
elif imc <25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('obesidade morbida')